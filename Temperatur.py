#!/usr/bin/python
# coding: utf8
import sys
import Adafruit_DHT
import MySQLdb
import thingspeak

#Get Temperatur from Sensor
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

#Save Data to a MySQL Database
db = MySQLdb.connect(host="localhost", user="Temperatur", passwd="Temperatur", db="Temperatur")
cur = db.cursor()
cur.execute("INSERT INTO Temperatur (temperature, humidity) VALUES (%s,%s)", (temperature, humidity,))
cur.close()
db.commit()

#Save Data to Thingspeak
channel = thingspeak.Channel(id=0000, write_key='N0TH1NG4U', api_key='R3LL7N0TH1NG4U')
channel.update({'field1': temperature, 'field2': humidity})
