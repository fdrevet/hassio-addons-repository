# Changelog

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


