#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import os,sys
from urllib.parse import urlparse
import paho.mqtt.client as paho
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

slot1_Sensor = 29
slot2_Sensor = 31
GPIO.setup(slot1_Sensor, GPIO.IN) 
GPIO.setup(slot2_Sensor, GPIO.IN) 

def on_connect(self, mosq, obj, rc):
        self.subscribe("Fan", 0)
        print("connected",mosq)
    
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

mqttc = paho.Client(client_id="mqttdashshub")                        # object declaration
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883') 
url = urlparse(url_str)
mqttc.connect(url.hostname, url.port)
print(url_str,url)

# Define delay between readings
delay = 5

while 1:
  rc = mqttc.loop()
  slot1_status = GPIO.input(slot1_Sensor)
  time.sleep(0.2)
  slot2_status = GPIO.input(slot2_Sensor)
  time.sleep(0.2)
  if (slot1_status == False):
   mqttc.publish("slot1","1")
   time.sleep(0.2)
  else:
    mqttc.publish("slot1","0")
    time.sleep(0.2)
    
  if (slot2_status == False):
   mqttc.publish("slot2","1")
   time.sleep(0.2)
  else:
    mqttc.publish("slot2","0")
    time.sleep(0.2)
