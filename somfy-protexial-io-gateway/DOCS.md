Welcome to "Somfy Protexial IO Gateway" add-on !



# Why this add-on ?

I don't own a [Tahoma Box](https://www.somfy.fr/produits/1811478/tahoma) and don't need/want one for the moment.



So, I wrote this add-on in order to let HASS.io and my alarm communicate bidirectionally.



# Disclaimers



## Unofficial add-on

This add-on is UNOFFICIAL.

This add-on does NOT rely on any [Somfy integration](https://www.home-assistant.io/integrations/somfy/).

I don't work for [Somfy Group](https://www.somfy-group.com) or am affiliated with them in any way.

"Somfy", "Somfy Protexial IO", and the icons of Somfy elements used in the documentation, are the property of [Somfy Group](https://www.somfy-group.com).



## Privacy

This add-on doesn't collect any data or personal information.

This add-on doesn't store any data, even locally, all data are managed in memory.

Persistent data are stored on chosen MQTT broker (for [MQTT integration](https://www.home-assistant.io/integrations/mqtt))



## Security

-



## Warranty

There is no warranty for the program, to the extent permitted by applicable law. except when otherwise stated in writing the copyright holders and/or other parties provide the program “as is” without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the program is with you. Should the program prove defective, you assume the cost of all necessary servicing, repair or correction.



# Design

To make HASS.io "talk" with your Somfy Protexial IO alarm, two add-ons will be needed :

- A “Somfy Protexial IO Proxy” add-on, exposing alarm’s data via a REST API (this add-on)
- A “Somfy Protexial IO Gateway” add-on, consuming “proxy” REST API data, and sending them to MQTT (commands can also be sent to add-on)



Why such design ?

- The “Somfy Protexial IO Proxy” monopolizes access to the alarm (web scrapping or POST requests)
- “Somfy Protexial IO Proxy” REST API can be used by gateway, but also other tools (like a "Somfy protexial IO Emulator", allowing to use Xiomfy Android App)



How it works ?

* “Somfy Protexial IO Gateway” consumes “Somfy Protexial IO Proxy” REST API to interact with the physical alarm



# Stability

It globally works well for my, but I still have some stability issue with web scrapping (sometimes the alarme is not responding, I guess scrapping every 5 seconds is too fast, will try with 10 seconds => can be configured in the addon)

I will work on it in the next days.



Also, It’s important to note that once the proxy add-on will work, it will be difficult to connect to the Alarm Web UI, since the proxy add-on do connect on the alarm, and try to reconnect if anything goes wrong (like a connection from alarm web UI, since only one user can be logged in at once)

I plan to release an “Emulator”, consuming “Gateway” REST API, and fixing this ennoying problem.



# Known issues

* When stoppping/restarting "Somfy Protexial IO Gateway" add-on on Rasperry PI, it can be necessary to physically reboot.



# Prerequisites



## Somfy Protexial IO Proxy connection

"Somfy Protexial IO Gateway" add-on requires a valid "Somfy Protexial IO Proxy" connection.



"Somfy Protexial IO Proxy" is an add-on who act like a proxy between physical alarm and consumers (like "Somfy Protexial IO Gateway")



## MQTT Broker connection

"Somfy Protexial IO Gateway" add-on requires a valid MQTT broker connection.



You can either use your own MQTT broker, or install a MQTT broker add-on such as "Mosquitto".



Plase note that only insecure connection are allowed yet, you can still specify an user name a password.



I plan to add TLS connection in a future version.



# Configuration

This add-on needs to be configured before being started.



You have to go to “Configuration” tab.



## Available options

Here are the available options :

```yaml
MqttBroker:
  Hostname: MQTT broker hostname or ip
  TcpPort: 1883
  Username: MQTT broker optional username
  Password: MQTT broker optional password
Proxy:
  Hostname: Somfy Protexial IO Proxy hostname or ip
  TcpPort: 8093
Hassio:
  MqttDiscoverPrefix: homeassistant
  EntitiesMqttPrefix: somfy_
  EntitiesMqttSuffix: ''
  EntitiesNamePrefix: 'Somfy - '
  EntitiesNameSuffix: ''
  ExposeGlobalStatus: true
  ExposeElements: true
  EnableMqttAlarmControlPanel: true
  MqttAlarmControlPanelState: homeassistant/spiog/state
  MqttAlarmControlPanelCommand: homeassistant/spiog/command
  EnableArmedBinarySensors: true
  EnableDisarmedBinarySensors: false
  EnableHealthcheckSensors: false
  RegisterBatteryBinarySensors : false
HassioMqttAlarmControlPanelCommands:
  ZoneAll: homeassistant/spiog/command
  ZoneA: homeassistant/spiog/command_a
  ZoneB: homeassistant/spiog/command_b
  ZoneC: homeassistant/spiog/command_c
HassioMqttAlarmControlPanelStates:
  ZoneAll: homeassistant/spiog/state
  ZoneA: homeassistant/spiog/state_a
  ZoneB: homeassistant/spiog/state_b
  ZoneC: homeassistant/spiog/state_c
HassioMqttAlarmControlPanelAllowDisarm:
  ZoneAll: true
  ZoneA: true
  ZoneB: true
  ZoneC: true
HassioEnableSwitches:
  ZoneAll: true
  ZoneA: true
  ZoneB: true
  ZoneC: true
HassioEntitiesIcons:
  - Key: '928367'
    Value: window
  - Key: alarm-triggered
    Value: problem
```



## MQTT Broker

MQTT broker settings. 

*Node : `MqttBroker`*



* `Hostname` : MQTT broker hostname or IP address

* `TcpPort` : MQTT broker TCP port (default 1883)

* `Username` : MQTT broker username (optional)

* `Password` : MQTT broker password (optional)



## Somfy Protexial IO Proxy

"Somfy Protexial IO Proxy" settings. 

*Node : `Proxy`*



* `Hostname` : Somfy Protexial IO Proxy hostname or IP address

* `TcpPort` : 8093



## Hassio

Hassio settings. 

*Node : `Hassio`*



* `MqttDiscoverPrefix` : MQTT prefix to discover entities, it must be the same than one configured on Hassio (default : "homeassistant")

* `EntitiesMqttPrefix` : MQTT prefix for entities (default : "somfy_")

* `EntitiesMqttSuffix` : MQTT prefix for entities (default : "")

* `EntitiesNamePrefix` : name prefix for entities (default : "Somfy - ")

* `EntitiesNameSuffix` : name suffix for entities (default : "")

* `ExposeGlobalStatus` : indicates whether the Somfy Protexial IO alarm's global status, should be exposed as Hassio entitites (default : true)

* `ExposeElements` : indicates whether the Somfy Protexial IO alarm's elements, should be exposed as Hassio entitites (default : true)

* `EnableMqttAlarmControlPanel` : enable [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : true)

* `MqttAlarmControlPanelState` : homeassistant/spiog/state

* `MqttAlarmControlPanelCommand` : homeassistant/spiog/command

* `EnableArmedBinarySensors` : indicates whether the armed binary sensors entities should be registered, or not (default : true) Please note that these entities have inverted logic (armed value will show "unlocked" in Hassio interface)

* `EnableDisarmedBinarySensors` : indicates whether the disarmed binary sensors entities should be registered, or not (default : false) These entities are consistent with Hassio logic (ie. armed value will show "locked" in Hassio interface)

* `EnableHealthcheckSensors` : indicates whether the "Somfy protexial IO Gateway" health related sensors, should be created, or not (default : false) If enabled, "Gateway operational" and "Proxy connectivity" Hassio sensors entities are registered.

* `RegisterBatteryBinarySensors` : indicates whether the Hassio battery binary sensors should be created, or not (default : false) If enabled (not recommended), devices will lost their battery indicators. Also, please note that battery binary sensors have inverted logic and must be handled as "battery low" in Hassio.



## Alarm Control panel commands

MQTT topics to handle arming/disarming commands sent from a Hassio [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt)

> We recommend not to change it, unless you changed `MqttDiscoverPrefix`

*Node : `HassioMqttAlarmControlPanelCommands`*



* `ZoneAll` : specify the MQTT topic that will handle an all zones (A, B, C) arming/disarming command sent from a [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/command" => "homeassistant/spiog/command")

* `ZoneA` : specify the MQTT topic that will handle a zone A arming/disarming command sent from a [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/command_a" => "homeassistant/spiog/command_a")

* `ZoneB ` : specify the MQTT topic that will handle a zone B arming/disarming command sent from a [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/command_b" => "homeassistant/spiog/command_b")

* `ZoneC ` : specify the MQTT topic that will handle a zone C arming/disarming command sent from a [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/command_c" => "homeassistant/spiog/command_c")



## Alarm Control panel states

MQTT topics that represent Hassio [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) states. 

> We recommend not to change it, unless you changed `MqttDiscoverPrefix`

*Node : `HassioMqttAlarmControlPanelStates`*



* `ZoneAll` : specify the MQTT topic that will represent all zones (A, B, C) arming/disarming state of [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/state" => "homeassistant/spiog/state")

* `ZoneA` : specify the MQTT topic that will represent zone A arming/disarming state of [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/state_a" => "homeassistant/spiog/state_a")

* `ZoneB` : specify the MQTT topic that will represent zone B arming/disarming state of [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/state_b" => "homeassistant/spiog/state_b")

* `ZoneC` : specify the MQTT topic that will represent zone C arming/disarming state of [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : "`MqttDiscoverPrefix`/spiog/state_c" => "homeassistant/spiog/state_c")



## Alarm Control allow disarm

Indicates, for each zone, if corresponding [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) can disarm alarm.

Please beware that disarming `could be unsecured` (ie. if no code is specified in [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt))

*Node : `HassioMqttAlarmControlPanelAllowDisarm`*



* `ZoneAll` : indicates whether all zones (A, B, C) can be disarmed at once, with [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : true)

* `ZoneA` : indicates whether zone A can be disarmed, with [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : true)

* `ZoneB` : indicates whether zone B can be disarmed, with [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : true)

* `ZoneC` : indicates whether zone C can be disarmed, with [MQTT Alarm Control panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) (default : true)



## Enable switches

Indicates, for each zone, if corresponding Hassio switch must be created. 

Please beware that arming/disarming switches **are unsecured** (ie. no code is required to arm/disarm alarm)

*Node : `HassioEnableSwitches`*



* `ZoneAll` : indicates whether all zones (A, B, C) Hassio entity switch will be register (default : true)
* `ZoneA` : indicates whether zone A Hassio entity switch will be register (default : true)

* `ZoneB` : indicates whether zone B Hassio entity switch will be register (default : true)

* `ZoneC` : indicates whether zone C Hassio entity switch will be register (default : true)



## Customize entities Icons

Since 0.6, you can customize most of generated Hassio entities icons, by specifying rules.



These rules are specified in ```HassioEntitiesIcons``` configuration node.



Each line  represent a Somfy element (by code) or Somfy property :

```yaml
...
HassioEntitiesIcons:
  "alarm-triggered": "door"
  "396245": "door"
  "396294": "window"
  "301181": "garage_door"
```



> Please note that HassioEntitiesIcons will be deprecated in future release, in order to have a possibility to customize more properties of Hassio entities



### Open/close icons

Open/close icons can be customize (default : ![Closed][image-closed] ![Opened][image-opened])  by specifying Somfy element code, and the wanted device class name (among those defined in https://www.home-assistant.io/integrations/binary_sensor)



This is possible for these Somfy elements :

* Door sensor ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_do.gif)

* Door window sensor ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_dovitre.gif)




### Motion icon

Motion icon can be customize (default : ![Motion][image-motion])  by specifying Somfy element code, and the wanted device class name (among those defined in https://www.home-assistant.io/integrations/binary_sensor)



This is possible for these Somfy elements :

* Motion detector![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/icon_camera_dm_on.gif)

* Motion detector with photo![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/icon_camera_dm_on.gif)



### Others binary sensors

Hassio entities icons generated for Somfy binary sensors, can be customized.



These properties are available for global status and some Somfy elements.



This is done :

* by specifying code in table
* and wanted device class name (among those defined in https://www.home-assistant.io/integrations/binary_sensor)

| Name            | Code              | Default icon                          |
| --------------- | ----------------- | ------------------------------------- |
| Battery         | battery           | ![Battery][image-battery] (battery)   |
| Box          | box               | ![Communication][image-communication] (connectivity) |
| Communication   | communication     | ![Communication][image-communication] (connectivity) |
| Doors/Windows   | doors-windows     | ![Closed][image-closed] ![Opened][image-opened] (opening) |



### Global status binary sensors

Hassio entities icons generated for Somfy global status binary sensors, can be customized.



These properties are available for global status and some Somfy elements.



This is done :

* by specifying code in table
* and wanted device class name (among those defined in https://www.home-assistant.io/integrations/binary_sensor)

| Name            | Code              | Default icon                          |
| --------------- | ----------------- | ------------------------------------- |
| Alarm (all) | alarm_all   | ![Shield][image-opened-lock] (lock) |
| Alarm (a) | alarm_a   | ![Shield][image-opened-lock] (lock)    |
| Alarm (b) | alarm_b  | ![Shield][image-opened-lock] (lock)    |
| Alarm (c) | alarm_c   | ![Shield][image-opened-lock] (lock) |
| Alarm disarmed (all) | alarm_all_disarmed   | ![Shield][image-opened-lock] (lock) |
| Alarm disarmed (a) | alarm_a_disarmed   | ![Shield][image-opened-lock] (lock)    |
| Alarm disarmed (b) | alarm_b_disarmed  | ![Shield][image-opened-lock] (lock)    |
| Alarm  disarmed(c) | alarm_c_disarmed   | ![Shield][image-opened-lock] (lock) |
| GSM OK          | gsm-communication | ![Communication][image-communication] (connectivity)   |



### Global status sensors

Hassio entities icons generated for Somfy global status sensors, can be customized.



These properties are available for global status.



This is done :

* by specifying code in table
* and wanted device class name (among those defined https://www.home-assistant.io/integrations/sensor)

| Name             | Code           | Default icon            |
| ---------------- | -------------- | ----------------------- |
| Gsm Signal       | gsm-signal     | ![Signal][image-signal] (signal_strength) |
| Gsm Signal (DBM) | gsm-signal-dbm | ![Signal][image-signal] (signal_strength) |



# Launch



## What happens

When "Somfy Protexial IO Gateway" is launched :

* it connects to MQTT broker
* and connects to "Somfy Protexial IO Proxy"



Once both connections are successful, it :

* fetch global status and elements details from "Somfy Protexial IO Proxy"
* create HASS.io devices

* create HASS.io entities
* constantly update HASS.io entities according to states fetched from "Somfy Protexial IO Proxy"



## HASS.io devices

Once the "Somfy Protexial IO Gateway" is launched :

* one Home Assistant "Somfy Protexial IO" device is created fro global status entities

* one Home Assistant "Somfy Protexial IO {Somfy element type} {Somfy element name}" device is created, per Somfy element



See entities section for more details.



## HASS.io Entities

Once the "Somfy Protexial IO Gateway" is launched, HASS.io entities are created :

* for Somfy Protexial IO global status
* for Somfy Protexial IO elements



#### Somfy Global status

One HASS.io entity is created per Somfy global status property, only if global status exposition is enabled in configuration (true by default)



All HASS.io entities will belong to device "Somfy Protexial IO".



Each HASS.io entity will be named as follow :

```
{EntitiesNamePrefix}{Global status property}{EntitiesNameSuffix}
```

Where :

* Entity prefix = "Somfy - " by default (can be configured)

* Global status property = English name

* Entity prefix = "" by default (can be configured)



So, not matter language is configured, the GSM signal (DBM) HASS.io entity full name will be :

```
Somfy - Gsm Signal (DBM)
```




#### Binary sensors (10)


| Icon                                            | Name            | Comment                                                      | Entity name                 |
| ----------------------------------------------- | --------------- | ------------------------------------------------------------ | --------------------------- |
| ![Shield][image-shield]                         | Alarm (all)     | true = all zone armed *                                      | ```somfy_alarm_all```       |
| ![Shield][image-shield]                         | Alarm (A)       | true = zone A armed *                                        | ```somfy_alarm_a```         |
| ![Shield][image-shield]                         | Alarm (B)       | true = zone B armed *                                        | ```somfy_alarm_b```         |
| ![Shield][image-shield]                         | Alarm (C)       | true = zone C armed *                                        | ```somfy_alarm_c```         |
| ![Shield][image-shield]                         | Alarm triggered | true = at least one element triggered an alarm               | ```somfy_alarm_triggered``` |
| ![Shield][image-shield]                         | Box             | true = at least one element have box issue                   | ```somfy_box```             |
| ![Communication][image-communication]           | Communication   | true = at least one element have communication issue         | ```somfy_communication```   |
| ![Battery][image-battery]                       | Battery         | true = at least one element have low battery **   | ```somfy_battery```         |
| ![Battery][image-battery]                       | Battery level   | 100 = all batteries ok, 0 = at least one element battery low | ```somfy_battery_level```   |
| ![Closed][image-closed] ![Opened][image-opened] | Doors/Windows   | true = at least one door/window is opened                    | ```somfy_doors_windows```   |
| ![Communication][image-communication]           | Gateway operational          | true = "Somfy Protexial IO Gateway" is successfully connected to "Somfy Protexial IO Proxy" and MQTT broker ***                      | ```somfy_gsm_ok```          |
| ![Communication][image-communication]           | GSM OK          | true = GSM is present and connected                          | ```somfy_gsm_ok```          |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```{MqttDiscoverPrefix}/binary_sensor/{Entity name}```



\* Only one "zone" can be armed at once

** Deprecated, "Battery level" is now recommended

*** "Somfy Protexial IO Gateway" being using MQTT integration to create Hassio entities, no update will be made to "Gateway operational" binary sensor, if MQTT broker connection is suddenly broken...

#### Sensors (2)

| Icon                    | Name             | Comment                                                      | Entity name                |
| ----------------------- | ---------------- | ------------------------------------------------------------ | -------------------------- |
| ![Signal][image-signal] | GSM Signal       | raw level : 0, 1, 2, 3, 4, 5 (5 = better signal)             | ```somfy_gsm_signal```     |
| ![Signal][image-signal] | GSM Signal (DBM) | Arbitrary DBM level : -70, -76, -83, -89, -96, -102 (-102 = better signal) | ```somfy_gsm_signal_dbm``` |
| ![Communication][image-communication]           | Proxy connectivity          | "Somfy Protexial IO Proxy" availability *                         | ```somfy_gsm_ok```          |

Entity id : ```sensor.{Entity name}```

MQTT topic : ```{MqttDiscoverPrefix}/sensor/{Entity name}```



\* "Somfy Protexial IO Proxy" availability values are :

* "NeverConnected" (not connected, and was never connected before)
* "Connected" (self explanatory)
* "Connecting" (try to connect, was never connected before)
* "Reconnecting" (try to connect, was connected before)
* "Disconnected" (not connected, was connected before)




#### Switches (4)

| Icon                       | Name        | Comment                 | Entity name           |
| -------------------------- | ----------- | ----------------------- | --------------------- |
| ![Lock][image-opened-lock] | Alarm (all) | true = all zone armed * | ```somfy_alarm_all``` |
| ![Lock][image-opened-lock] | Alarm (A)   | true = zone A armed *   | ```somfy_alarm_a```   |
| ![Lock][image-opened-lock] | Alarm (B)   | true = zone B armed *   | ```somfy_alarm_b```   |
| ![Lock][image-opened-lock] | Alarm (C)   | true = zone C armed *   | ```somfy_alarm_c```   |

Entity id : ```switch.{Entity name}```

MQTT topic : ```{MqttDiscoverPrefix}/switch/{Entity name}```



\* Only one "zone" can be armed at once



### Somfy Elements

HASS.io entities are created according to each type of Somfy element, only if element exposition is enabled in configuration (true by default)



All HASS.io entities will belong to their device "Somfy Protexial IO {Somfy element type} {Somfy element name}".



Please note that not all Somfy elements are yet managed, contact me if your Somfy element is missing, or if a property is missing.

 

Each HASS.io entity name will be constructed as follow :

```
{EntitiesNamePrefix}{Element type} - {Entity label} - {Entity property}{EntitiesNameSuffix}
```

* EntitiesNamePrefix = "Somfy - " by default (can be configured)
* Element type = name of Somfy element type in your alarm web ui (depends of configured language)
* Element label = name that you gave to your Somfy element in alarm web ui
* Entity property = name of Somfy element property (```Alarm triggered```, ```Battery, Box```, ```Communication```, ```Doors/Windows```, ```Gsm OK```, ```Gsm Signal```, ```Gsm Signal (DBM)```)
* EntitiesNameSuffix = "" by default (can be configured)

> So, with French language configuration, the "Bureau" door/window Somfy element will be named by default :
>
> ```
> Somfy - DO Vitre - Bureau
> ```

 

Each HASS.io entity id will be constructed as follow :

```
{EntitiesNamePrefix}{Element type} - {Entity label}{EntitiesNameSuffix}
```

* Entity prefix = "Somfy - " by default (can be configured)

* Element type = name of Somfy element type in your alarm web ui (depends of configured language)

* Element label = name that you gave to your Somfy element in alarm web ui

* Entity prefix = "" by default (can be configured)

> So, with French language configuration, the "Bureau" door/window Somfy element box property, will be named by default :
>
> ```
> somfy_do_vitre_bureau_box
> ```



Each HASS.io entity MQTT root topic will be constructed as follow :


```
{MqttDiscoverPrefix}/binary_sensor/{EntitiesMqttPrefix}{Entity code}_{Entity name}{EntitiesMqttSuffix}
```

* MqttDiscoverPrefix = see configuration
* EntitiesMqttPrefix = see configuration
* Entity code = numeric code of Somfy Protexial IO element
* Entity name = see table
* EntitiesMqttSuffix = see configuration

> So, don't matter the language configuration is, the office door/window (code 2987263) Somfy element MQTT root topic will be by default :
>
> ```
> homeassistant/binary_sensor/somfy_typedo_2987263
> ```



#### Door sensor (5) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_do.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                           | Name            | Comment                               | Entity name           |
| ---------------------------------------------- | --------------- | ------------------------------------- | --------------------- |
| ![Alarm][image-shield]                         | Alarm triggered | true = alarm triggered                | ```alarm_triggered``` |
| ![Battery][image-battery]                      | Battery         | true = battery low, false = battery OK * | ```battery```         |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Box][image-shield]                           | Box             | true = box OK/not snatched            | ```box```             |
| ![Communication][image-communication]          | Communication   | true = communication OK               | ```communication```   |
| ![Closed][image-closed] ![Opened][image-opened] | Door state      | true = opened, false = closeds        | ```door_window```     |



\* Deprecated, "Battery level" is now recommended



#### Door window sensor (5) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_dovitre.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                           | Name              | Comment                               | Entity name           |
| ---------------------------------------------- | ----------------- | ------------------------------------- | --------------------- |
| ![Alarm][image-shield]                         | Alarm triggered   | true = alarm triggered                | ```alarm_triggered``` |
| ![Battery][image-battery]                      | Battery           | true = battery low, false = battery OK * | ```battery```         |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Box][image-shield]                           | Box               | true = box OK/not snatched            | ```box```             |
| ![Communication][image-communication]          | Communication     | true = communication OK               | ```communication```   |
| ![Closed][image-closed] ![Opened][image-opened] | Door/Window state | true = opened, false = closeds        | ```door_window```     |



\* Deprecated, "Battery level" is now recommended



#### Keyboard (3) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_keyb.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name         |
| ------------------------------------- | ------------- | ------------------------------------- | ------------------- |
| ![Battery][image-battery]             | Battery       | true = battery low, false = battery OK * | ```battery```       |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Box][image-shield]                  | Box           | true = box OK/not snatched            | ```box```           |
| ![Communication][image-communication] | Communication | true = communication OK               | ```communication``` |



\* Deprecated, "Battery level" is now recommended



#### Indoor siren (3) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_sirenint.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name         |
| ------------------------------------- | ------------- | ------------------------------------- | ------------------- |
| ![Battery][image-battery]             | Battery       | true = battery low, false = battery OK * | ```battery```       |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Box][image-shield]                  | Box           | true = box OK/not snatched            | ```box```           |
| ![Communication][image-communication] | Communication | true = communication OK               | ```communication``` |



\* Deprecated, "Battery level" is now recommended



#### Motion detector (5) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/icon_camera_dm_on.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                  | Name            | Comment                               | Entity name           |
| ------------------------------------- | --------------- | ------------------------------------- | --------------------- |
| ![Alarm][image-shield]                | Alarm triggered | true = alarm triggered                | ```alarm_triggered``` |
| ![Battery][image-battery]             | Battery         | true = battery low, false = battery OK * | ```battery```         |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Box][image-shield]                  | Box             | true = box OK/not snatched            | ```box```             |
| ![Communication][image-communication] | Communication   | true = communication OK               | ```communication```   |
| ![Motion][image-motion]               | Motion          | true = detected                       | ```motion```          |



\* Deprecated, "Battery level" is now recommended



#### Motion detector with photo (5) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/icon_camera_dm_on.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                  | Name            | Comment                               | Entity name           |
| ------------------------------------- | --------------- | ------------------------------------- | --------------------- |
| ![Alarm][image-shield]                | Alarm triggered | true = alarm triggered                | ```alarm_triggered``` |
| ![Battery][image-battery]             | Battery         | true = battery low, false = battery OK * | ```battery```         |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Box][image-shield]                  | Box             | true = box OK/not snatched            | ```box```             |
| ![Communication][image-communication] | Communication   | true = communication OK               | ```communication```   |
| ![Motion][image-motion]               | Motion          | true = detected                       | ```motion```          |



\* Deprecated, "Battery level" is now recommended



#### Outdoor siren (3) ![img](https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/p_sirenext.gif)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name         |
| ------------------------------------- | ------------- | ------------------------------------- | ------------------- |
| ![Battery][image-battery]             | Battery       | true = battery low, false = battery OK * | ```battery```       |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Shield][image-shield]               | Box           | true = box OK/not snatched            | ```box```           |
| ![Communication][image-communication] | Communication | true = communication OK               | ```communication``` |



\* Deprecated, "Battery level" is now recommended



#### Smoke detector (3)

All Somfy element properties are creating a HASS.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name         |
| ------------------------------------- | ------------- | ------------------------------------- | ------------------- |
| ![Battery][image-battery]             | Battery       | true = battery low, false = battery OK * | ```battery```       |
| ![Battery][image-battery]                      | Battery level         | 100 = battery OK, 0 = battery low | ```battery_level```         |
| ![Alarm][image-shield]                | Box           | true = box OK/not snatched            | ```box```           |
| ![Communication][image-communication] | Communication | true = communication OK               | ```communication``` |



\* Deprecated, "Battery level" is now recommended



#### Tahoma (1)

All Somfy element properties are creating a HASS.io binary sensor entity.s

| Icon                                  | Name          | Comment                 | Entity name         |
| ------------------------------------- | ------------- | ----------------------- | ------------------- |
| ![Communication][image-communication] | Communication | true = communication OK | ```communication``` |



## REST API

“Somfy Protexial IO Gateway” doesn't expose REST API yet.



# Alarm panel integration

You can use [Manual Alarm Control Panel](https://www.home-assistant.io/integrations/manual/) or [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/) (recommended)



## Manual Alarm Control Panel

"Somfy Protexial IO Gateway" can be used with [Manual Alarm Control Panel](https://www.home-assistant.io/integrations/manual/) and some automation, as described in article.



Simply use "Alarm (All)" switch or binary sensor (you don't need to specify all entities, unless you don't expose global status)



Please note this panel is not the most natural, since "Somfy Protexial IO" alarm physically manage triggers by itself : [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/) is recommended.



## MQTT Alarm Control Panel

"Somfy Protexial IO Gateway" is compatible with [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) since version 0.5.0.



You can manage zones since version 0.6 :

* all zones (ABC) armed
* zone A armed

* zone B armed

* zone C armed



Also, and still with version 0.6, physical alarm arming/disarming changes are dynamically reflected to  [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt) !



### All zones (ABC)

Add Hassio configuration entry like :

```yaml
- platform: mqtt
  name: Somfy Protexial IO (all)
  code: '1234'
  state_topic: homeassistant/spiog/state
  command_topic: homeassistant/spiog/command
```



And configure your "Somfy Protexial IO Gateway" configuration with :

```yaml
...
Hassio:
  EnableMqttAlarmControlPanel: true
  MqttAlarmControlPanelState: homeassistant/spiog/state
  MqttAlarmControlPanelCommand: homeassistant/spiog/command
```



### Zone A

Add Hassio configuration entry like :

```yaml
- platform: mqtt
  name: Somfy Protexial IO (zone a)
  code: '1234'
  state_topic: homeassistant/spiog/state_a
  command_topic: homeassistant/spiog/command_a
```



And configure your "Somfy Protexial IO Gateway" configuration with :

```yaml
...
Hassio:
  EnableMqttAlarmControlPanel: true
  MqttAlarmControlPanelStates:
    ZoneA: homeassistant/spiog/state_a
  MqttAlarmControlPanelCommands:
    ZoneA: homeassistant/spiog/command_a
```



### Zone B

Add Hassio configuration entry like :

```yaml
- platform: mqtt
  name: Somfy Protexial IO (zone b)
  code: '1234'
  MqttAlarmControlPanelStates:
    ZoneB: homeassistant/spiog/state_b
  MqttAlarmControlPanelCommands:
    ZoneB: homeassistant/spiog/command_b
```



And configure your "Somfy Protexial IO Gateway" configuration with :

```yaml
...
Hassio:
  EnableMqttAlarmControlPanel: true
  MqttAlarmControlPanelStates:
    ZoneB: homeassistant/spiog/state_b
  MqttAlarmControlPanelCommands:
    ZoneB: homeassistant/spiog/command_b
```



### Zone C

Add Hassio configuration entry like :

```yaml
- platform: mqtt
  name: Somfy Protexial IO (zone c)
  code: '1234'
  state_topic: homeassistant/spiog/state_c
  command_topic: homeassistant/spiog/command_c
```



And configure your "Somfy Protexial IO Gateway" configuration with :

```yaml
...
Hassio:
  EnableMqttAlarmControlPanel: true
  MqttAlarmControlPanelStates:
    ZoneC: homeassistant/spiog/state_c
  MqttAlarmControlPanelCommands:
    ZoneC: homeassistant/spiog/command_c
```




[image-shield]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/shield.png	"Shield"

[image-battery]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/battery.png	"Battery"

[image-signal]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/signal.png	"Signal"

[image-lightning]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/lightning.png	"Lightning"

[image-opened-lock]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/opened-lock.png	"Opened lock"

[image-communication]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/communication.png	"Communication"

[image-opened]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/opened.png	"Closed"

[image-closed]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/closed.png	"Opened"

[image-motion]: https://github.com/fdrevet/hassio-addons-repository/raw/master/somfy-protexial-io-gateway/images/motion.png	"Motion"

