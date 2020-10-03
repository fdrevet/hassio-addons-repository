# Changelog

## 0.6.0

- Added and improved logs

- Improved alarm connection job source code

## 0.5.0

- Added logs when stopping add-on

- Quartz jobs are now unscheduled, when stopping add-on

- When Somfy Protexial IO elements are fetched them for the first time, details are outputted in logs

## 0.4.0

Fixed "'{item label}' doesn't exists" error in logs, causing whole elements fetch to fail.

Now, a warning is outputted in logs if an element type is not handled (will be improved in next releases), and the valid elements are returned (please contact me to handle these elements)

## 0.3.0

- Now indicating in which order security table must be stored (settings)

- Now working with French and German Somfy Protexial IO alarms.

- Now working with new elements :
  - typeremote2
  - typetecfumee
  - typetahoma

## 0.2.0

- Fixed "ports_description" (settings)

- Upgraded .NET third party libraries

- Fixed global status's camera label

## 0.1.0

- Initial release, working with my French Somfy Protexial IO alarm.


