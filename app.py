import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

client = paho.Client()
client.username_pw_set("username", "password")
client.on_connect = on_connect
client.connect("broker.mqtt-dashboard.com", 1883)
