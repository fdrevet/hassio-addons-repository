Welcome to "Somfy Protexial IO Gateway" add-on !



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

-



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

* “Somfy Protexial IO Gateway” consumes “Somfy Protexial IO Proxy” REST API to interact with the physical alarm



# MQTT Broker connection







# REST API
“Somfy Protexial IO Gateway” doesn't expose REST API yet.



# Devices

Once the "Somfy Protexial IO Gateway" is launched :

* one Home Assistant "Somfy Protexial IO" device is created fro global status entities

* one Home Assistant "Somfy Protexial IO {Somfy element type} {Somfy element name}" device is created, per Somfy element

See entities section for more details.

# Entities

A lot of entities will be created once the "Somfy Protexial IO Gateway" is launched :

## Global status

Hass.io entities are created for global status, only if global status exposition is enabled (true by default)

- 4 switches
  - ![Lock][image-opened-lock] Alarm (true = armed, false = disarmed)
  - ![Lock][image-opened-lock] Alarm A (true = armed, false = disarmed)
  - ![Lock][image-opened-lock] Alarm B (true = armed, false = disarmed)
  - ![Lock][image-opened-lock] Alarm C (true = armed, false = disarmed)
- 2 sensors
  - ![Signal][image-signal] GSM raw level :  0, 1, 2, 3 (3 = better signal)
  - ![Signal][image-signal] GSM DBM level : ??, ??; ??; -94 (-94 = better signal)
- 10 binary sensors
  - ![Zen2][image-shield] Alarm (true = armed, false = disarmed)
  - ![Zen2][image-shield] Alarm A (true = armed, false = disarmed)
  - ![Zen2][image-shield] Alarm B (true = armed, false = disarmed)
  - ![Zen2][image-shield] Alarm C (true = armed, false = disarmed)
  - ![zz][image-battery] Open/close state (true = at least one door open)
  - ![azeer][image-shield] Alarm triggered (true = at least one element triggered alarm)
  - ![zzerfs][image-communication] Communication state (true = at least one element have communication issue)
  - ![zzerfs][image-communication] GSM OK (true = GSM is present and connected)
  - ![azeer][image-shield] Box state (true = at least one element have box issue)
  - ![zz][image-battery] Battery state (true = at least one element have battery issue)

## Elements

Hass.io entities are created according to each type of Somfy element, only if element exposition is enabled (true by default)

Not all types of items are yet managed, please contact me if your Somfy element is missing, or if a property is missing.

### Door sensor

- ![Alarm][image-shield] Alarm (true = alarm triggered)
- ![Battery][image-battery] Battery (true = battery OK)
- ![Box][image-shield] Box (true = box OK/not snatched)
- ![Communication][image-communication] Communication (true = communication OK)
- ![Closed][image-closed] ![Opened][image-opened] Door state (true = opened, false = closed)

### Door window sensor

- ![][image-shield] Alarm (true = box OK/not snatched)
- ![][image-battery] Battery (true = battery OK)
- ![][image-shield] Box (true = box OK/not snatched)
- ![][image-communication] Communication (true = communication OK)
- ![][image-closed] ![][image-opened] Door/Window state (true = opened, false = closed)

### Keyboard

- ![][image-battery] Battery (true = battery OK)
- ![][image-shield] Box (true = box OK/not snatched)
- ![][image-communication] Communication (true = communication OK)

### Indoor siren

* ![][image-battery] Battery (true = battery OK)
* ![][image-shield] Box (true = box OK/not snatched)
* ![][image-communication] Communication (true = communication OK)

### Motion detector

* ![azeer][image-shield] Alarm (true = alarm triggered)
* ![][image-battery] Battery (true = battery OK)
* ![][image-shield] Box (true = box OK/not snatched)
* ![][image-communication] Communication (true = communication OK)
* ![][image-motion] Motion (true = detected)

### Motion detector (image)

* ![azeer][image-shield] Alarm (true = alarm triggered)
* ![zz][image-battery] Battery (true = battery OK)
* ![azeer][image-shield] Box (true = box OK/not snatched)
* ![zzerfs][image-communication] Communication (true = communication OK)
* ![errt][image-motion] Motion (true = detected)

### Outdoor siren

* ![zz][image-battery] Battery (true = battery OK)
* ![azeer][image-shield] Box (true = box OK/not snatched)
* ![zzerfs][image-communication] Communication (true = communication OK)

### Smoke detector

* ![azeer][image-shield] Alarm (true = box OK/not snatched)
* ![zz][image-battery] Battery (true = battery OK)
* ![zzerfs][image-communication] Communication (true = communication OK)

### Tahoma

* ![azeer][image-shield] Alarm (true = box OK/not snatched)
* ![zz][image-battery] Battery (true = battery OK)
* ![zzerfs][image-communication] Communication (true = communication OK)

# Stability

It globally works well for my, but I still have some stability issue with web scrapping (sometimes the alarme is not responding, I guess scrapping every 5 seconds is too fast, will try with 10 seconds => can be configured in the addon)

I will work on it in the next days.



Also, It’s important to note that once the proxy add-on will work, it will be difficult to connect to the Alarm Web UI, since the proxy add-on do connect on the alarm, and try to reconnect if anything goes wrong (like a connection from alarm web UI, since only one user can be logged in at once)

I plan to release an “Emulator”, consuming “Gateway” REST API, and fixing this ennoying problem.

# Configuration

This add-on doesn't rely on any Somfy integration.



This add-on requires to be configured.



You have to go to “Configuration” tab (same apply for "Somfy Protexial IO Proxy")



Required informations are :




[image-shield]: .\images\shield.png	"Shield"

[image-battery]: .\images\battery.png	"Battery"

[image-signal]: .\images\signal.png	"Signal"

[image-lightning]: .\images\lightning.png	"Lightning"

[image-opened-lock]: .\images\opened-lock.png	"Opened lock"

[image-communication]: .\images\communication.png	"Communication"

[image-opened]: .\images\opened.png	"Closed"

[image-closed]: .\images\closed.png	"Opened"

[image-motion]: .\images\motion.png	"Motion"

