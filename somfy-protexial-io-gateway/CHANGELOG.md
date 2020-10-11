# Changelog

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


