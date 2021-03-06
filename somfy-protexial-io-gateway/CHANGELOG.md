# Changelog

## 0.8.1

Somfy element "typetrans" (Central) now have following sensors :

* Battery

* Communication
* Alarm Triggered
* Box



Somfy element "typebadgerfid" (RFID badge) now have following sensor :

* Alarm Triggered



Somfy element "typeremote2" (two buttons remote control) now have following sensor :

* Alarm Triggered



Somfy element "typeremote4" (four buttons remote control) now have following sensor :

* Alarm Triggered



Updated documentation accordingly.



Source code maintenance.



## 0.8.0

Added running sensors, values :

* Running

* Paused

> Great to see running sensor, but why not switches not change state from Hassio ?
>
> It was expected to add this feature in this release, but change "Running/Paused" require to be connected as "i" (installer) user, while you have to be connected as "u" (user) user to arm and disarm alarm... It would be possible to temporary connect as "i" user and come back to "u" user, but without possibility to arm/disarm alarm during this delay. Anyway, if this feature is added, it would be handled by the "Somfy Protexial IO Proxy".



Somfy elements are now set online/offline, depending of their running property in web user interface (ie. running/paused), except for running sensors.



Added "Hassio > RegisterBatteryBinarySensors" option (default false) :

* true : existing "battery" binary sensors are kept in the interface (in addition of "battery level" sensors)

* false : existing "battery" binary sensors are removed (only "battery level" sensors are available)

Using only battery sensors (ie. removing battery binary sensors) show battery indicators in devices.



Fixed Somfy elements alarm triggered binary sensor, who was inverted.



Added missing sensors :

* "Keyboard", "External siren", "Internal siren" Somfy elements have now "alarm triggered" binary sensors
* "Keyboard" has now battery sensor



"Gateway operational" and "Proxy connectivity" entities are now unregistered if "Hassio > EnableHealthcheckSensors" option is false.



Big documentation update.



## 0.7.0

"Somfy Protexial IO Gateway" is now more stable and resilient, regarding the "Somfy Protexial IO Proxy" availability/unavailability :

* It waits for an available "Somfy Protexial IO Proxy" to register entities and update them
* if "Somfy Protexial IO Proxy" became unavailable, Hassio entities are marked as unavailable too
* if "Somfy Protexial IO Proxy" became available again, Hassio entities are marked as available



To clarify the current status of "Somfy Protexial IO Gateway" (not REST API being developed yet), two optional Hassio entities has been added :

* "Gateway operational" : binary sensor indicating whether the Gateway is operational or not ("Somfy Protexial IO Proxy" available and MQTT broker connected *)  
* "Proxy connectivity" : sensor with following values
  * "NeverConnected" (not connected, and was never connected before)
  * "Connected" (self explanatory)
  * "Connecting" (try to connect, was never connected before)
  * "Reconnecting" (try to connect, was connected before)
  * "Disconnected" (not connected, was connected before)

These sensors are disabled by default, to enable them, just set "Hassio > EnableHealthcheckSensors" node to "true" in settings.

> "Somfy Protexial IO Gateway" being using MQTT integration to create Hassio entities, no update will be made to "Gateway operational" binary sensor, if MQTT broker connection is suddenly broken...



Added "battery level" sensors in addition of existing "battery" binary sensors.

Since "Somfy Protexial IO" alarm don't provides % values for batteries (only 1/0), values are 100 (full) or 0 (low)

Beware : existing "battery" binary sensors rather means "battery low" (OFF = battery "full", ON = battery low)

I plan to make "battery-level" sensors works with devices.



Fixed existing bug that did not update "box" and "alarm-triggered" elements, when their state were updated from Somfy Protexial IO alarm.



Fixed battery sensor documentation (was inverted for Somfy elements)

## 0.6.1

Fixed unretained offline/online messages, causing elements to be marked as "unavailable" when restarting Home Assistant.

## 0.6.0

Zones can now be managed in [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) :

* all zones (ABC) armed
* zone A armed

* zone B armed

* zone C armed



Physical alarm arming/disarming, are dynamically reflected to  [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (zones : all, a, b, c)



Home Assistant switches for zones All, A, B or C, can now be enabled/disabled.



Existing Home Assistant binary sensors for zones All, A, B or C alarm armed status, can now be enabled/disabled (default : enabled)



Added Home Assistant binary sensors for zones All, A, B or C.

These new binary sensors can now be enabled/disabled (default : disabled)



Alarm disarming from Home Assistant switches for zones All, A, B or C, can now be enabled/disabled.



Created Home Assistant entities, are now set to :

* online, when add-on is started

* offline, when add-on is stopped




Created Hassio entities icons icons can now be customized.



Fixed configuration sample.

## 0.5.0

- Added support for MQTT Alarm Control Panel (Hassio => Somfy Protexial IO alarm)

## 0.4.2

- Changes in values of Hass.io entities are now kept via MQTT, this fixes the problem of loss of state when restarting Hass.io

## 0.4.1

- Upgraded documentation
- Fixed GSM DBM values

## 0.4.0

- A Hassio device is created for each Somfy elements, previously only a global Somfy Protexial IO device was created for global status entities

- Hassio entities are updated only if they have been registered first

- Fixed possible multiple global status Hassio entities registration (multi-threading)

- Changed Hassio entities's MQTT topics for global status (somfy_global-status_{name} => somfy_{name})

- Improved Hassio entities creation, depending of Somfy elements types

  - Somfy elements "type_dm", "type_dmv", "typedo", "typedovitre", "typetecfumee" => a Hassio entity "Alarm triggered" is created
  - Somfy elements "type_dm", "type_dmv", "typedo", "typedovitre", "typekeyb", "typesirenext", "typesirenint" => a Hassio entity "Box" is created
  - Somfy elements "type_dm", "type_dmv", "typedo", "typedovitre", "typekeyb", "typesirenext", "typesirenint", "typetecfumee" => a Hassio entity "Battery" is created
  - Somfy elements "type_dm", "type_dmv", "typedo", "typedovitre", "typekeyb", "typesirenext", "typesirenint", "typetahoma", "typetecfumee" => a Hassio entity "Communication" is created

- now checking that MQTT client is connected, when discovering a Somfy element (bug)

- Added new "Hassio" configuration section :

  "Hassio": {
  		"MqttDiscoverPrefix": "homeassistant",
  		"EntitiesMqttPrefix": "somfy_",
  		"EntitiesMqttSuffix": "",
  		"EntitiesNamePrefix": "Somfy - ",
  		"EntitiesNameSuffix": "",
  		"ExposeGlobalStatus": "true",
  		"ExposeElements": "true"
  	}

- updated README.md

## 0.3.0

- Fixed typo (trigered => triggered) when generating global status entities

- Improved source code

- Added and improved logs

## 0.2.0

- Fixed "Somfy Protexial IO" device creation (one per switch before)

- Now unscheduling Quartz jobs, when stopping engine

- Added and improved logs

## 0.1.0

- Initial release, working with my French Somfy Protexial IO alarm.

