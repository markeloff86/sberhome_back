import time

import paho.mqtt.client as mqtt
import motion


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("mqtt_client", "sberhack")
client.connect("192.168.43.150", 1883, 60)
client.loop_start()

while True:
    client.publish("pi/motion", motion.is_motioned(7))
