# Webservice test for Gardena smart API

Testscript von Gardena [https://developer.husqvarnagroup.cloud/apis/GARDENA+smart+system+API#/readme](https://developer.husqvarnagroup.cloud/apis/GARDENA+smart+system+API#/readme)
 zum Aufruf der Gardena Smart API ohne ioBroker. 

Test script from Gardena [https://developer.husqvarnagroup.cloud/apis/GARDENA+smart+system+API#/readme](https://developer.husqvarnagroup.cloud/apis/GARDENA+smart+system+API#/readme)
to call Gardena Smart API without integration to ioBroker

Dient zum Debuggen bei Problemen mit der Schnittstelle oder 
den darin übertragenen Daten.

Used for debugging problems with the interface or
the data transmitted in it.



Das Script `ws_test.py` auf den Computer kopieren.
Darin muss man gleich in den oberen Zeilen die eigenen Daten eintragen. 

Copy the script `ws_test.py` to the computer.
You have to enter your own data in the top lines.

```
# account specific values
USERNAME = 'myUserEmail'
PASSWORD = 'myUserPassword'
API_KEY =  'myApplicationApiKey'

```

Aufruf des scriptes mit

Call script with 

```
python3 ws_test.py
```

Bitte posted nirgends die vollständigen Ausgaben des Scriptes, es stehen EURE token in der Ausgabe. 
I.d.R. reichen mir die Angaben ab der folgenden Zeile 

Please don't post the complete output of the script, YOUR token are in the output.
Usually the information starting from the following line is enough for me 

```
### connected ###
```

Zur Info bei evtl. fehlenden Modulen für die Nutzung von *python3*. Ich musste bei mir folgendes installieren:

For information about any missing modules for the use of *python3*. I had to install the following for me:

```
pi@ioBroker:~ $ sudo apt-get install python3
...

pi@ioBroker:~ $ sudo apt-get install python3-pip
...

pi@ioBroker:~ $ pip3 install requests
...

pi@ioBroker:~ $ pip3 install websocket-client
...

pi@ioBroker:~ $  python3 --version
Python 3.7.3

pi@ioBroker:~ $ pip3 --version
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
```


<!--- SVN: $Rev: 2124 $ $Date: 2020-05-23 16:11:22 +0200 (Sa, 23 Mai 2020) $ --->