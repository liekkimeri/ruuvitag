from flask import Flask,json
import os
import datetime
from flask_cors import CORS,cross_origin
import sqlite3 as lite
import sys
import pytz
from ruuvitag_sensor.ruuvi import RuuviTagSensor

app = Flask(__name__)
cors = CORS(app, resources={r"/getWeatherData": {"origins": "*"}})
cors = CORS(app, resources={r"/getWeatherDataCharts": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getWeatherData")
def getWeatherData():
    
	
	weatherList =[]
	tagList = ['F6:DB:7F:5E:C8:62','F1:15:2E:FC:0C:3A','EF:28:0A:7D:E1:1D','E9:7A:A6:0B:51:1E','F0:DE:F8:93:AF:A2']
	
	for tag in tagList:
	
		con = lite.connect('database.db')
		with con:    
			
			sqlCmd = "SELECT temperature,pressure,humidity,timestamp from ruuvitagData where ruuvitagId = '" + tag + "' ORDER BY id DESC limit 1"
			cur = con.cursor()    
			cur.execute(sqlCmd)

			rows = cur.fetchall()
		 

			for row in rows:
				data = row
				weatherDict = {
						'Id':tag ,
						'Temperature':data[0],
						'Humidity':data[2],
						'Pressure':data[1]}

			weatherList.append(weatherDict)
			
		con.close()
	
	return json.dumps(weatherList)
	
@app.route("/getWeatherDataCharts")
def getWeatherDataCharts():
	weatherList =[]
	tz = pytz.timezone('Europe/Helsinki')
	con = lite.connect('database.db')
	with con:
		
		
		yesterday= datetime.datetime.now(tz=tz)- datetime.timedelta(days = 1)
		tomorro =  datetime.datetime.now(tz=tz)+ datetime.timedelta(days = 1)
		print(yesterday)
		print(tomorro)
		sqlCmd = "select ruuvitagID,temperature,pressure,humidity,timestamp   from ruuvitagData where timestamp  >= '"+ yesterday.strftime("%Y-%m-%d") +"' AND timestamp <= '" + tomorro.strftime("%Y-%m-%d") + "'"
		print(sqlCmd)
		
		cur = con.cursor()
		cur.execute(sqlCmd)
		
		rows = cur.fetchall()

		for row in rows:
			data = row
			weatherDict = {
					'Id':data[0] ,
					'Temperature':data[1],
					'Humidity':data[3],
					'Pressure':data[2],
					'Time':data[4]}
			weatherList.append(weatherDict)

		
			
	con.close()
	
	return json.dumps(weatherList)
		
	


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
