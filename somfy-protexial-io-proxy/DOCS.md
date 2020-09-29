Welcome to "Somfy Protexial IO Proxy" add-on !



# Why this add-on ?

I don't own a Tahoma Box and don't need/want one for the moment. So, I wrote this add-on in order to let Hass.IO and my alarm communicate bidirectionally.



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



# Issue with physical alarm

It’s important to note that once the “Somfy Protexial IO Proxy” add-on is started and connected, it's quite difficult to connect to the alarm  web user interface (from a browser or application doing also web scrapping...)



Indeed, “Somfy Protexial IO Proxy” add-on connect on the alarm, and try to reconnect if anything goes wrong.



The alarm web user interface only accepts one logged in user at a time.



I plan to release an “Emulator”, also consuming “Somfy Protexial IO Proxy” REST API, as a workaround for this annoying problem.



# REST API

“Somfy Protexial IO Proxy” expose data with a custom REST API, available on your HASS.io server's port 8193 (default)



Here are some links to check that all is working (no swagger available yet)



## Version

http://hostname:8193

Return static JSON with REST API version and description

```
{“version”:“1.0.0”,“description”:""}
```



## Alarm’s global status

http://hostname:8193/api/status

Return alarm's global status, as JSON



## Alarm’s elements

http://hostname:8193/api/elements

Return alarm's elements as JSON



## Alarm’s connection status

http://hostname:8193/api/connection/status

Return alarm's connection status as JSON



# Sensors

"Somfy Protexial IO Proxy" doesn't create any sensor in Hassio.

It exposes a REST API, consumed by "Somfy Protexial IO Gateway" (who creates sensors), see "Design" section to understand by.



# Configuration

This add-on requires to be configured.



You have to go to “Configuration” tab (same apply for "Somfy Protexial IO Gateway")



Required informations are :

- alarm hostname (or IP)
- alarm TCP port (default is 80)
- password of user “u” (same that you use when connecting to your alarm)
- security table values (in order to automatically connect to the alarm)

User “u” can be changed (with “i” for example) but I suggest to not change it (I’ll probbaly remove this setting)

Here is how it look like :



![image](https://community-assets.home-assistant.io/optimized/3X/5/8/58f073589554bb28bf4ce5df7663704c497ed715_2_591x500.png)

