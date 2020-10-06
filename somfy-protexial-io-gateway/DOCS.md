Welcome to "Somfy Protexial IO Gateway" add-on !



# Why this add-on ?

I don't own a Tahoma Box and don't need/want one for the moment.



So, I wrote this add-on in order to let Hass.IO and my alarm communicate bidirectionally.



# Disclaimers



## Unofficial add-on

This add-on is UNOFFICIAL.

This add-on doesn't rely on any Somfy integration.

I don't work for Somfy Group or am affiliated with them in any way.



## Privacy

I do not collect data or personal information.

All the data are kept on your HASS.io installation.



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

"Somfy Protexial IO Gateway" add-on doesn't rely on any Somfy integration.



This add-on requires to be configured.



You have to go to “Configuration” tab (same apply for "Somfy Protexial IO Proxy")



Required informations are :



# Launch



## Hass.io devices

Once the "Somfy Protexial IO Gateway" is launched :

* one Home Assistant "Somfy Protexial IO" device is created fro global status entities

* one Home Assistant "Somfy Protexial IO {Somfy element type} {Somfy element name}" device is created, per Somfy element



See entities section for more details.



## Hass.io Entities

Once the "Somfy Protexial IO Gateway" is launched, Hass.io entities are created.



#### for Somfy Global status

One Hass.io entity is created per Somfy global status property, only if global status exposition is enabled in configuration (true by default)



All Hass.io entities will belong to device "Somfy Protexial IO".



Each Hass.io entity will be named as follow :

```
{Entity prefix}{Global status property}{Entity suffix}
```

Where :

* Entity prefix = "Somfy - " by default (can be configured)

* Global status property = English name

* Entity prefix = "" by default (can be configured)



So, not matter language is configured, the GSM signal (DBM) Hass.io entity full name will be :

```
Somfy - Gsm Signal (DBM)
```




#### Binary sensors (10)


| Icon                                           | Name            | Comment                                              | Entity name                 |
| ---------------------------------------------- | --------------- | ---------------------------------------------------- | --------------------------- |
| ![Shield][image-shield]                        | Alarm (all)     | true = all zone armed *                              | ```somfy_alarm_all```       |
| ![Shield][image-shield]                        | Alarm (A)       | true = zone A armed *                                | ```somfy_alarm_a```         |
| ![Shield][image-shield]                        | Alarm (B)       | true = zone B armed *                                | ```somfy_alarm_b```         |
| ![Shield][image-shield]                        | Alarm (C)       | true = zone C armed *                                | ```somfy_alarm_c```         |
| ![Shield][image-shield]                        | Alarm triggered | true = at least one element triggered an alarm       | ```somfy_alarm_triggered``` |
| ![Shield][image-shield]                        | Box             | true = at least one element have box issue           | ```somfy_box```             |
| ![Communication][image-communication]          | Communication   | true = at least one element have communication issue | ```somfy_communication```   |
| ![Battery][image-battery]                      | Battery         | true = at least one element have battery issue       | ```somfy_battery```         |
| ![Closed][image-closed]![Opened][image-opened] | Doors/Windows   | true = at least one door/window is opened            | ```somfy_doors_windows```   |
| ![Communication][image-communication]          | GSM OK          | true = GSM is present and connected                  | ```somfy_gsm_ok```          |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



\* Only one "zone" can be armed at once



#### Sensors (2)

| Icon                    | Name             | Comment                                  | Entity name                |
| ----------------------- | ---------------- | ---------------------------------------- | -------------------------- |
| ![Signal][image-signal] | GSM Signal       | raw level 0, 1, 2, 3 (3 = better signal) | ```somfy_gsm_signal```     |
| ![Signal][image-signal] | GSM Signal (DBM) | ??, ??; ??; -94 (-94 = better signal)    | ```somfy_gsm_signal_dbm``` |

Entity id : ```sensor.{Entity name}```

MQTT topic : ```homeassistant/sensor/{Entity name}```




#### Switches (4)

| Icon                       | Name        | Comment                 | Entity name           |
| -------------------------- | ----------- | ----------------------- | --------------------- |
| ![Lock][image-opened-lock] | Alarm (all) | true = all zone armed * | ```somfy_alarm_all``` |
| ![Lock][image-opened-lock] | Alarm (A)   | true = zone A armed *   | ```somfy_alarm_a```   |
| ![Lock][image-opened-lock] | Alarm (B)   | true = zone B armed *   | ```somfy_alarm_b```   |
| ![Lock][image-opened-lock] | Alarm (C)   | true = zone C armed *   | ```somfy_alarm_c```   |

Entity id : ```switch.{Entity name}```

MQTT topic : ```homeassistant/switch/{Entity name}```



\* Only one "zone" can be armed at once



### for Somfy Elements

Hass.io entities are created according to each type of Somfy element, only if element exposition is enabled in configuration (true by default)



All Hass.io entities will belong to their device "Somfy Protexial IO {Somfy element type} {Somfy element name}".



Not all Somfy elements are yet managed, please contact me if your Somfy element is missing, or if a property is missing.

 

Each Hass.io entity name will be constructed as follow :

```
{Entity prefix}{Element type} - {Entity label} - {Entity property}{Entity suffix}
```

* Entity prefix = "Somfy - " by default (can be configured)
* Element type = name of Somfy element type in your alarm web ui (depends of configured language)
* Entity property = name of Somfy element property (```Alarm triggered```, ```Battery, Box```, ```Communication```, ```Doors/Windows```, ```Gsm OK```, ```Gsm Signal```, ```Gsm Signal (DBM)```)
* Element label = name that you gave to your Somfy element in alarm web ui
* Entity prefix = "" by default (can be configured)

> So, with French language configuration, the "Bureau" door/window Somfy element will be named by default :
>
> ```
> Somfy - DO Vitre - Bureau
> ```

 

Each Hass.io entity id will be constructed as follow :

```
{Entity prefix}{Element type} - {Entity label}{Entity suffix}
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



Each Hass.io entity MQTT root topic will be constructed as follow :


```
{MQTT discover prefix}/{MQTT entity type}/{MQTT entity prefix}{Somfy element type}_{Somfy element code}{MQTT entity suffix}
```

* MQTT discover prefix = "homeassistant" by default (can be configured)
* MQTT Entity type = Hass.io entity type (```binary_sensor```, ```sensor```, ```switch```)
* MQTT Entity prefix = "somfy_" by default (can be configured)
* Somfy element type = ```type_dm```, ```type_dmv```, ```typedo```, ```typedovitre```, ```typekeyb```, ```typesirenext```, ```typesirenint```, ```typetahoma```, ```typetecfumee```
* Somfy element code = Numeric Somfy element code
* MQTT Entity prefix = "" by default (can be configured)

> So, don't matter the language configuration is, the office door/window Somfy element MQTT root topic will be by default :
>
> ```
> homeassistant/binary_sensor/somfy_typedo_2987263
> ```

 

#### Door sensor (5)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                           | Name            | Comment                               | Entity name                                               |
| ---------------------------------------------- | --------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Alarm][image-shield]                         | Alarm triggered | true = alarm triggered                | ```alarm_triggered```                                     |
| ![Battery][image-battery]                      | Battery         | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Box][image-shield]                           | Box             | true = box OK/not snatched            |                                                           |
| ![Communication][image-communication]          | Communication   | true = communication OK               |                                                           |
| ![Closed][image-closed]![Opened][image-opened] | Door state      | true = opened, false = closeds        |                                                           |

Entity id : ```binary_sensor.somfy_{Entity type}_{Entity name}```

* Entity prefix = "Somfy - " by default (can be configured)
* Element type = name of Somfy element type in your alarm web ui (depends of configured language)
* Element name = see table
* Entity prefix = "" by default (can be configured)

MQTT topic : ```homeassistant/binary_sensor/{Entity code}```

Where :

* Entity code = numeric code of Somfy element



#### Door window sensor (5)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                           | Name              | Comment                               | Entity name                                               |
| ---------------------------------------------- | ----------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Alarm][image-shield]                         | Alarm triggered   | true = alarm triggered                |                                                           |
| ![Battery][image-battery]                      | Battery           | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Box][image-shield]                           | Box               | true = box OK/not snatched            |                                                           |
| ![Communication][image-communication]          | Communication     | true = communication OK               |                                                           |
| ![Closed][image-closed]![Opened][image-opened] | Door/Window state | true = opened, false = closeds        |                                                           |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Keyboard (3)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name                                               |
| ------------------------------------- | ------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Battery][image-battery]             | Battery       | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Box][image-shield]                  | Box           | true = box OK/not snatched            |                                                           |
| ![Communication][image-communication] | Communication | true = communication OK               |                                                           |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Indoor siren (3)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name                                               |
| ------------------------------------- | ------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Battery][image-battery]             | Battery       | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Box][image-shield]                  | Box           | true = box OK/not snatched            |                                                           |
| ![Communication][image-communication] | Communication | true = communication OK               |                                                           |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Motion detector (5)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                  | Name            | Comment                               | Entity name                                               |
| ------------------------------------- | --------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Alarm][image-shield]                | Alarm triggered | true = alarm triggered                |                                                           |
| ![Battery][image-battery]             | Battery         | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Box][image-shield]                  | Box             | true = box OK/not snatched            |                                                           |
| ![Communication][image-communication] | Communication   | true = communication OK               |                                                           |
| ![Motion][image-motion]               | Motion          | true = detected                       |                                                           |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Motion detector with photo (5)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                  | Name            | Comment                               | Entity name                                               |
| ------------------------------------- | --------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Alarm][image-shield]                | Alarm triggered | true = alarm triggered                |                                                           |
| ![Battery][image-battery]             | Battery         | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Box][image-shield]                  | Box             | true = box OK/not snatched            |                                                           |
| ![Communication][image-communication] | Communication   | true = communication OK               |                                                           |
| ![Motion][image-motion]               | Motion          | true = detected                       |                                                           |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Outdoor siren (3)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name                                               |
| ------------------------------------- | ------------- | ------------------------------------- | --------------------------------------------------------- |
| ![Battery][image-battery]             | Battery       | true = battery OK, false = battery KO | ```somfy_{Element type}_{Element Name}_alarm_triggered``` |
| ![Shield][image-shield]               | Box           | true = box OK/not snatched            | ```somfy_{Element type}_{Element Name}_box```             |
| ![Communication][image-communication] | Communication | true = communication OK               | ```somfy_{Element type}_{Element Name}_communication```   |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Smoke detector (3)

All Somfy element properties are creating a Hass.io binary sensor entity.

| Icon                                  | Name          | Comment                               | Entity name |
| ------------------------------------- | ------------- | ------------------------------------- | ----------- |
| ![Alarm][image-shield]                | Alarm         | true = box OK/not snatched            |             |
| ![Battery][image-battery]             | Battery       | true = battery OK, false = battery KO |             |
| ![Communication][image-communication] | Communication | true = communication OK               |             |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



#### Tahoma (1)

All Somfy element properties are creating a Hass.io binary sensor entity.s

| Icon                                  | Name          | Comment                 | Entity name |
| ------------------------------------- | ------------- | ----------------------- | ----------- |
| ![Communication][image-communication] | Communication | true = communication OK |             |

Entity id : ```binary_sensor.{Entity name}```

MQTT topic : ```homeassistant/binary_sensor/{Entity name}```



## REST API

“Somfy Protexial IO Gateway” doesn't expose REST API yet.





# Misc



## Alarm panel integration

You can either use [Manual Alarm Control Panel](https://www.home-assistant.io/integrations/manual/), [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/)



### Manual Alarm Control Panel

"Somfy Protexial IO Gateway" can be easily used with [Manual Alarm Control Panel](https://www.home-assistant.io/integrations/manual/) and some automation, as described.



### MQTT Alarm Control Panel

"Somfy Protexial IO Gateway" is not yet compatible with [MQTT Alarm Control Panel](https://www.home-assistant.io/integrations/alarm_control_panel.mqtt), stay in touch.




[image-shield]: .\images\shield.png	"Shield"

[image-battery]: .\images\battery.png	"Battery"

[image-signal]: .\images\signal.png	"Signal"

[image-lightning]: .\images\lightning.png	"Lightning"

[image-opened-lock]: .\images\opened-lock.png	"Opened lock"

[image-communication]: .\images\communication.png	"Communication"

[image-opened]: .\images\opened.png	"Closed"

[image-closed]: .\images\closed.png	"Opened"

[image-motion]: .\images\motion.png	"Motion"

