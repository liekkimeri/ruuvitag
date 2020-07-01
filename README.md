# ruuvitag
Tallentaan dataa SQLite tietokantaan ja näyttää viimeiset mittaustulokset websivulla

## Käytetyt elementit
  - [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
  - [Python 2](https://docs.python.org/2/)
  - [RuuviTag Sensor Python Package](https://github.com/ttu/ruuvitag-sensor) by [Tomi Tuhkanen](https://github.com/ttu)
  - [Flask microframework](http://flask.pocoo.org/)
  - [SQLite 3 database](https://docs.python.org/3.6/library/sqlite3.html#module-sqlite3)
  - [nginx](https://www.nginx.com/resources/wiki/)

## Kannan luonti:

Kannan luonti onnistuu helposti kommennolla "sqlite3 database.db < schema.sql"

## ruuvitag.py 
Muuta tag-muuttujan sisältä vastaamaan sinun ruuviTagin mac-osoitteita.

## ruuvitagServer.py
Muuta tag-muuttujan sisältä vastaamaan sinun ruuviTagin mac-osoitteita.

## www-sivut
Asenna ngix ja kopio html-kansion sisältö kansioon /var/www/html
Muokkaa requestURL-muuttojan arvo vastaan osoitetta mitä flask-serveri kuuntelee
