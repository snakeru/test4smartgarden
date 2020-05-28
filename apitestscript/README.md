# APITEST for Gardena smart API

Testscript zum Aufruf der Gardena Smart API ohne ioBroker. 
Dient zum Debuggen bei Problemen mit der Schnittstelle oder 
den darin übertragenen Daten.

Das Script `apitest.py` auf den Computer kopieren.
Darin muss man gleich in den oberen Zeilen die eigenen Daten eintragen. 

```
# account specific values
USERNAME = 'myUserEmail'
PASSWORD = 'myUserPassword'
API_KEY =  'myApplicationApiKey'

```

Aufruf des scriptes mit
```
python3 apitest.py
```

Bitte posted nirgends die vollständigen Ausgaben des Scriptes, es stehen EURE token in der Ausgabe. 

I.d.R. reichen mir die Angaben ab einer Zeile 

```
### connected ###
```

aus. Diese Ausgaben am besten per PN senden und nicht im Forum. 
Nicht dass da doch noch irgendwo Zugangsdaten drinstehen.

Zur Info bei evlt. fehlenden Modulen für die Nutzung von *python3*. Ich musste bei mir folgendes installieren:
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