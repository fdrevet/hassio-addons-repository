import logging
import requests

import voluptuous as vol
import traceback
from datetime import timedelta

from .APSystemsSocket import APSystemsSocket, APSystemsInvalidData
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.discovery import load_platform
from homeassistant.const import CONF_HOST, CONF_SCAN_INTERVAL
from homeassistant.helpers.entity import Entity
from homeassistant import config_entries, exceptions
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN, CONF_SSID, CONF_WPA_PSK, CONF_CACHE

PLATFORMS = [ "sensor", "binary_sensor", "switch" ]

# handle all the communications with the ECUR class and deal with our need for caching, etc

class WiFiSet():
    SSID = ""
    WPA = ""
    CACHE = 5
U_WiFiSet = WiFiSet()    

class ECUR():
    def __init__(self, ipaddr, ssid, wpa, cache):
        self.ecu = APSystemsSocket(ipaddr)
        self.ipaddr = ipaddr
        self.ssid = ssid
        self.wpa = wpa
        self.cache = cache
        self.cache_count = 0
        self.data_from_cache = False
        self.querying = True
        self.ecu_restarting = False
        self.cached_data = {}
        U_WiFiSet.SSID = self.ssid
        U_WiFiSet.WPA = self.wpa
        U_WiFiSet.CACHE = self.cache

    def stop_query(self):
        self.querying = False

    def start_query(self):
        self.querying = True

    def use_cached_data(self, msg):
        # we got invalid data, so we need to pull from cache
        self.error_msg = msg
        self.cache_count += 1
        self.data_from_cache = True

        if self.cache_count == U_WiFiSet.CACHE:
            _LOGGER.warning(f"Communication with the ECU failed after {U_WiFiSet.CACHE} repeated attempts.")
            data = {'SSID': U_WiFiSet.SSID, 'channel': 0, 'method': 2, 'psk_wep': '', 'psk_wpa': U_WiFiSet.WPA}
            _LOGGER.debug(f"Data sent with URL: {data}")
            # Determine ECU type to decide ECU restart (for ECU-C and ECU-R with sunspec only)
            if (self.cached_data.get("ecu_id", None)[0:3] == "215") or (self.cached_data.get("ecu_id", None)[0:4] == "2162"):
                url = 'http://' + str(self.ipaddr) + '/index.php/management/set_wlan_ap'
                headers = {'X-Requested-With': 'XMLHttpRequest'}
                try:
                    get_url = requests.post(url, headers=headers, data=data)
                    _LOGGER.debug(f"Attempt to restart ECU gave as response: {str(get_url.status_code)}.")
                    self.ecu_restarting = True
                except Exception as err:
                    _LOGGER.warning(f"Attempt to restart ECU failed with error: {err}. Querying is stopped automatically.")
                    self.querying = False
            else:
                # Older ECU-R models starting with 2160
                _LOGGER.warning("Try manually power cycling the ECU. Querying is stopped automatically, turn switch back on after restart of ECU.")
                self.querying = False
            
        if self.cached_data.get("ecu_id", None) == None:
            _LOGGER.debug(f"Cached data {self.cached_data}")
            raise UpdateFailed(f"Unable to get correct data from ECU, and no cached data. See log for details, and try power cycling the ECU.")

        return self.cached_data

    def update(self):
        data = {}
        
        # if we aren't actively quering data, pull data form the cache
        # this is so we can stop querying after sunset
        if not self.querying:
            _LOGGER.debug("Not querying ECU due to query=False")
            data = self.cached_data
            self.data_from_cache = True

            data["data_from_cache"] = self.data_from_cache
            data["querying"] = self.querying
            return self.cached_data

        _LOGGER.debug("Querying ECU...")
        try:
            data = self.ecu.query_ecu()
            _LOGGER.debug("Got data from ECU")

            # we got good results, so we store it and set flags about our
            # cache state
            if data["ecu_id"] != None:
                self.cached_data = data
                self.cache_count = 0
                self.data_from_cache = False
                self.ecu_restarting = False
                self.error_message = ""
            else:
                msg = f"Using cached data from last successful communication from ECU. Error: no ecu_id returned"
                _LOGGER.warning(msg)
                data = self.use_cached_data(msg)

        except APSystemsInvalidData as err:
            msg = f"Using cached data from last successful communication from ECU. Invalid data error: {err}"
            if str(err) != 'timed out':
                _LOGGER.warning(msg)
            data = self.use_cached_data(msg)

        except Exception as err:
            msg = f"Using cached data from last successful communication from ECU. Exception error: {err}"
            _LOGGER.warning(msg)
            data = self.use_cached_data(msg)

        data["data_from_cache"] = self.data_from_cache
        data["querying"] = self.querying
        data["restart_ecu"] = self.ecu_restarting
        _LOGGER.debug(f"Returning {data}")

        if data.get("ecu_id", None) == None:
            raise UpdateFailed(f"Somehow data doesn't contain a valid ecu_id")
            
        return data

async def update_listener(hass, config):

    # Handle options update being triggered by config entry options updates
    _LOGGER.debug(f"Configuration updated: {config.as_dict()}")
    host = config.data[CONF_HOST]
    ssid = config.data[CONF_SSID]
    wpa = config.data[CONF_WPA_PSK]
    cache = config.data[CONF_CACHE]
    ecu = ECUR(host, ssid, wpa, cache)
    ecu.__init__(host, ssid, wpa, cache)

async def async_setup_entry(hass, config):
    # Setup the APsystems platform """
    hass.data.setdefault(DOMAIN, {})

    host = config.data[CONF_HOST]
    interval = timedelta(seconds=config.data[CONF_SCAN_INTERVAL])
    # Default new parameters that haven't been set yet from previous integration versions
    try:
        cache = config.data[CONF_CACHE]
        ssid = config.data[CONF_SSID]
        wpa = config.data[CONF_WPA_PSK]
    except:
        cache = 5
        ssid = "ECU-WiFi_SSID"
        wpa = "myWiFipassword"
    ecu = ECUR(host, ssid, wpa, cache)

    async def do_ecu_update():
        return await hass.async_add_executor_job(ecu.update)

    coordinator = DataUpdateCoordinator(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_method=do_ecu_update,
            update_interval=interval,
    )

    hass.data[DOMAIN] = {
        "ecu" : ecu,
        "coordinator" : coordinator
    }
    await coordinator.async_config_entry_first_refresh()

    device_registry = dr.async_get(hass)

    device_registry.async_get_or_create(
        config_entry_id=config.entry_id,
        identifiers={(DOMAIN, f"ecu_{ecu.ecu.ecu_id}")},
        manufacturer="APSystems",
        suggested_area="Roof",
        name=f"ECU {ecu.ecu.ecu_id}",
        model=ecu.ecu.firmware,
        sw_version=ecu.ecu.firmware,
    )

    inverters = coordinator.data.get("inverters", {})
    for uid,inv_data in inverters.items():
        model = inv_data.get("model", "Inverter")
        device_registry.async_get_or_create(
            config_entry_id=config.entry_id,
            identifiers={(DOMAIN, f"inverter_{uid}")},
            manufacturer="APSystems",
            suggested_area="Roof",
            name=f"Inverter {uid}",
            model=inv_data.get("model")
        )
    await hass.config_entries.async_forward_entry_setups(config, PLATFORMS)
    config.async_on_unload(config.add_update_listener(update_listener))
    return True

async def async_unload_entry(hass, config):
    unload_ok = await hass.config_entries.async_unload_platforms(config, PLATFORMS)
    coordinator = hass.data[DOMAIN].get("coordinator")
    ecu = hass.data[DOMAIN].get("ecu")
    ecu.stop_query()
    if unload_ok:
        hass.data[DOMAIN].pop(config.entry_id)
    return unload_ok
