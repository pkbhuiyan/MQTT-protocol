import paho.mqtt.client as paho
from random import *
import time


def on_publish(client, userdata, mid):
    print("mid: " + str(mid))



def weather_temperature_gen():
    temperature_value = randint(1, 20)
    return temperature_value


client = paho.Client()
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    temperature = weather_temperature_gen()
    (rc, mid) = client.publish("encyclopedia/temperature", str(temperature), qos = 1)
    time.sleep(30)
