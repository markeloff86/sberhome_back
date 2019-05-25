import paho.mqtt.client as mqtt
import json
import time, threading


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("18.223.169.60", 1883, 60)
client.loop_start()

def foo():
    motion = {"MOCK_motionDetected": True}
    client.publish("test", json.dumps(motion))
    threading.Timer(10, foo).start()


try:
    foo()
except KeyboardInterrupt:
    print(" Quit")