Welcome to Somfy Protexial IO Proxy add-on !



# Why this add-on ?

I don't own a Tahoma Box and don't need/want one for the moment. So, I wrote this add-on in order to let Hass.IO and my alarm communicate bidirectionally.



# Disclaimers



## Unofficial add-on

This add-on is UNOFFICIAL, I don't work for Somfy Group or am affiliated with them in any way.



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



# REST API



“Somfy Protexial IO Proxy” expose data with a custom REST API, available on your HASS.io server's port 8193 (default)



Here are some links to check that all is working (no swagger available yet)

* http://hostname:8193s => should return {“version”:“1.0.0”,“description”:""}
* http://hostname:8193/api/status => return alarm’s global status as json
* http://hostname:8193/api/elements => return alarm’s elements as json



# Sensors



A lot of sensors are created :

- Global status will provide :
  - Alarm (activate/unactivate)
  - Alarm A (activate/unactivate)
  - Alarm B (activate/unactivate)
  - Alarm C (activate/unactivate)
  - open/close state (true = at least one door open)
  - alarm triggered (true = at least one element triggered alarm)
  - communication state (true = at least one element have communication issue)
  - box state (true = at least one element have box issue)
  - battery state (true = at least one element have battery issue)
  - GSM raw level (numeric)
  - GSM DBM level (numeric)
- each door sensor (typedo, typedovitre) will be named “Somfy - {element name} - Opened” and provide :
  - open/close state (true/false)
  - alarm triggered state (true/false)
  - communication state (true/false)
  - box state (true/false)
  - battery state (true/false)

It globally works well for my, but I still have some stability issue with web scrapping (sometimes the alarme is not responding, I guess scrapping every 5 seconds is too fast, will try with 10 seconds => can be configured in the addon)

I will work on it in the next days.



Also, It’s important to note that once the proxy add-on will work, it will be difficult to connect to the Alarm Web UI, since the proxy add-on do connect on the alarm, and try to reconnect if anything goes wrong (like a connection from alarm web UI, since only one user can be logged in at once)

I plan to release an “Emulator”, consuming “Gateway” REST API, and fixing this ennoying problem.





## Configuration



My add-ons don’t rely on Somfy integration.

For the Proxy, you have to go to “Configuration” tab (same apply for Gateway)

Required informations are :

- alarm hostname (or IP)
- alarm TCP port (default is 80)
- password of user “u” (same that you use when connecting to your alarm)
- security table values (in order to automatically connect to the alarm)

User “u” can be changed (with “i” for example) but I suggest to not change it (I’ll probbaly remove this setting)

Here is how it look like :



![image](https://community-assets.home-assistant.io/optimized/3X/5/8/58f073589554bb28bf4ce5df7663704c497ed715_2_591x500.png)

