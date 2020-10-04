Welcome to "Somfy Protexial IO Proxy" add-on !



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

Add-on's REST API is NOT secured for the moment (only HTTP protocol, and no kind of authentication)

Please be sure that it's not exposed to Internet.



## Warranty

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.



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

Some stability issues can arise with web scrapping (sometimes the alarm is not responding)

Scrapping every 5 seconds maybe too fast, anyway this can be configured (see Configuration section)



# Sensors

"Somfy Protexial IO Proxy" doesn't create any sensor in Hassio.

It exposes a REST API, consumed by "Somfy Protexial IO Gateway" (who creates sensors), see "Design" section to understand by.



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