from flask import Flask,json
import time
import os
from datetime import datetime
from flask_cors import CORS,cross_origin
import sqlite3 as lite
import sys

from ruuvitag_sensor.ruuvi import RuuviTagSensor

app = Flask(__name__)
cors = CORS(app, resources={r"/getWeatherData": {"origins": "*"}})
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

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
