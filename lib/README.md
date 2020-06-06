# api.js test for Gardena smart API

Test einer Spezialversion von `api.js`

- mower id mit Suffix
- invalid date
- PAUSE for SERVICE_VALVE
  - To skip automatic operation until specified time, the currently active 
    operation might or might not be cancelled (depends on device model) use string 
    `PAUSE_<number_of_seconds>`, e.g. `PAUSE_86400` to pause for 24 hours


**ioBroker smartgarden Adapter stoppen**

Bitte die Datei austauschen im `lib`-Verzeichnis. Für einen Raspberry mit typischer ioBroker Installation
wird das vmtl. so aussehen.


```
pi@iobroker:~ $ cd /opt/iobroker/
pi@iobroker:/opt/iobroker $ cd node_modules/iobroker.smartgarden
pi@iobroker:/opt/iobroker/node_modules/iobroker.smartgarden $ cd lib
pi@iobroker:/opt/iobroker/node_modules/iobroker.smartgarden/lib $ ls -l
total 108
-rwxrwxrwx+ 1 iobroker iobroker   491 May  3 11:51 adapter-config.d.ts
-rwxrwxrwx+ 1 iobroker iobroker 75237 May 31 22:27 api.js
-rwxrwxrwx+ 1 iobroker iobroker  9860 May  3 11:51 history.js
-rwxrwxrwx+ 1 iobroker iobroker 12002 May  3 11:51 predefdp.js
-rwxrwxrwx+ 1 iobroker iobroker  3083 May  3 11:51 tools.js

```

dann die bestehende `api.js` retten (umbenennen)

```
pi@iobroker:/opt/iobroker/node_modules/iobroker.smartgarden/lib $ mv api.js api.js.old
pi@iobroker:/opt/iobroker/node_modules/iobroker.smartgarden/lib $

```

Dann die Datei in das Verzeichnis kopieren und kontrollieren ob sie da ist

```
pi@iobroker:/opt/iobroker/node_modules/iobroker.smartgarden/lib $ ls -l
total 108
-rwxrwxrwx+ 1 iobroker iobroker   491 May  3 11:51 adapter-config.d.ts
-rwxrwxrwx+ 1 iobroker iobroker 75261 May 31 23:52 api.js
-rwxrwxrwx+ 1 iobroker iobroker 75237 May 31 22:27 api.js.old
-rwxrwxrwx+ 1 iobroker iobroker  9860 May  3 11:51 history.js
-rwxrwxrwx+ 1 iobroker iobroker 12002 May  3 11:51 predefdp.js
-rwxrwxrwx+ 1 iobroker iobroker  3083 May  3 11:51 tools.js
```

Datum + Dateigrößen können abweichen.


**ioBroker smartgarden Adapter starten**



