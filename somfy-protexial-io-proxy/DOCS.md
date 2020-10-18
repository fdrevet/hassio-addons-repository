Welcome to "Somfy Protexial IO Proxy" add-on !



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

## Security

Add-on's REST API is NOT secured for the moment (only HTTP protocol, and no kind of authentication)

Please be sure that it's not exposed to Internet.



## Warranty

There is no warranty for the program, to the extent permitted by applicable law. except when otherwise stated in writing the copyright holders and/or other parties provide the program “as is” without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the program is with you. Should the program prove defective, you assume the cost of all necessary servicing, repair or correction.



## Issue with physical alarm

It’s important to note that once the “Somfy Protexial IO Proxy” add-on is started and connected, it's quite difficult to connect to the alarm  web user interface (from a browser or application doing also web scrapping...)



Indeed, “Somfy Protexial IO Proxy” add-on connect on the alarm, and try to reconnect if anything goes wrong.



The alarm web user interface only accepts one logged in user at a time.



I plan to release an “Emulator”, also consuming “Somfy Protexial IO Proxy” REST API, as a workaround for this annoying problem.



# Design

To make HASS.io "talk" with your Somfy Protexial IO alarm, two add-ons will be needed :

- A “Somfy Protexial IO Proxy” add-on, exposing alarm’s data via a REST API (this add-on)
- A “Somfy Protexial IO Gateway” add-on, consuming “proxy” REST API data, and sending them to MQTT (commands can also be sent to add-on)



Why such design ?

- The “Somfy Protexial IO Proxy” monopolizes access to the alarm (web scrapping or POST requests)
- “Somfy Protexial IO Proxy” REST API can be used by gateway, but also other tools (like a "Somfy protexial IO Emulator", allowing to use Xiomfy Android App)



How it works ?

* “Somfy Protexial IO Proxy” communicate with the alarm, through the built-in alarm's web ui
* HTTP GET to get data (web scrapping)
* HTTP POST to send data



# Stability

It globally works well for my, but I still have some stability issue with web scrapping (sometimes the alarme is not responding, I guess scrapping every 5 seconds is too fast, will try with 10 seconds => can be configured in the addon)

I will work on it in the next days.



Also, It’s important to note that once the proxy add-on will work, it will be difficult to connect to the Alarm Web UI, since the proxy add-on do connect on the alarm, and try to reconnect if anything goes wrong (like a connection from alarm web UI, since only one user can be logged in at once)

I plan to release an “Emulator”, consuming “Gateway” REST API, and fixing this ennoying problem.



# Hass.io devices

"Somfy Protexial IO Proxy" doesn't create any devices in your Hass.io.



It exposes a REST API, consumed by "Somfy Protexial IO Gateway" (who creates devices), see "Design" section to understand why.



# Hass.io entities

"Somfy Protexial IO Proxy" doesn't create any entities in your Hass.io.



It exposes a REST API, consumed by "Somfy Protexial IO Gateway" (who creates entities), see "Design" section to understand why.



# Configuration

This add-on needs to be configured, before being started.



Go to “Configuration” tab.



Instructions :

```
Alarm:
  Hostname: hostname or ip of your Somfy Protexial IO alarm
  TcpPort: tcp port of your Somfy Protexial IO alarm
  Username: 'u'
  Password: password of 'u' user
  SecurityTable: >-
    A1 B1 C1 D1 E1 F1
    A2 B2 C2 D2 E2 F2
    A3 B3 C3 D3 E3 F3
    A4 B4 C4 D4 E4 F4
    A5 B5 C5 D5 E5 F5
Proxy:
  Language: language used to connect to Somfy Protexial IO alarms's web ui (fr, gb, nl, it, de)
  AlarmConnectionRefresh: Interval in seconds, at which a connection will be attempted (default 30)
  AlarmStateRefresh: Interval in seconds, at which alarm's global status and elements will be fetched (default 5)
```



Factitious example :

```
Alarm:
  Hostname: alarm.home
  TcpPort: 80
  Username: 'u'
  Password: '9287'
  SecurityTable: >-
    9287 3876 3251 8293 2675 6876
    4829 5438 8266 9276 8256 3897
    2098 3887 2376 1322 2987 3764
    2876 6257 9283 2983 1876 3876
    3786 7378 9387 1287 3902 2786
Proxy:
  Language: 'fr'
  AlarmConnectionRefresh: 30
  AlarmStateRefresh: 5
```



# REST API

“Somfy Protexial IO Proxy” expose data with a custom REST API, available on your HASS.io server's port 8193 (default)



## Swagger

Swagger JSON is available at :

* Added Swagger (http://hostname:port/swagger/v1/swagger.json)



Swagger UI is available at :

* Added Swagger UI (http://hostname:port/swagger)



Here are some links to check that all is working (no swagger available yet)



## cURL samples



### Get API version

```
curl http://hostname:8193
```



### Get alarm’s global status

```
curl http://hostname:8193/api/status
```



### Alarm’s elements

```
curl http://hostname:8193/api/elements
```



### Get alarm’s connection status

```
curl http://hostname:8193/api/connection/status
```



### Arm  alarm

```
curl -X POST -d "" http://hostname:8193/api/alarm/deactivate
```



### Disarm  alarm

```
curl -X POST -d "" http://hostname:8193/api/alarm/activate/{zone}
```

> Where {zone} is : A, B, C or ABC.