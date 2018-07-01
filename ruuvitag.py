import time
import os
import sqlite3 as sql


from datetime import datetime
import pytz

from ruuvitag_sensor.ruuvitag import RuuviTag

def insertRuuvitagData(temperature,pressure,humidity,ruuvitagId,timestamp):

    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO ruuvitagData (temperature,pressure,humidity,ruuvitagId,timestamp) VALUES (?,?,?,?,?)", (temperature,pressure,humidity,ruuvitagId,timestamp))
    con.commit()
    con.close()
    print('insert ruuvitagdata database')


# Change here your own device's mac-address
tagList = ['F6:DB:7F:5E:C8:62','F1:15:2E:FC:0C:3A','EF:28:0A:7D:E1:1D','E9:7A:A6:0B:51:1E','F0:DE:F8:93:AF:A2']
print('Starting')
tz = pytz.timezone('Europe/Helsinki')

while True:
	
	
	for tag in tagList:
		sensor = RuuviTag(tag)
		data = sensor.update()
	
		insertRuuvitagData(data['temperature'],data['pressure'],data['humidity'],tag,datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M'))
		print(tag)

    # Wait for 60 seconds and start over again
	try:
		time.sleep(300)
	except KeyboardInterrupt:
        # When Ctrl+C is pressed execution of the while loop is stopped
		print('Exit')
		break
