import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

# client.username_pw_set("mqtt_client", "pass")
client.connect("18.223.169.60", 1883, 60)
client.loop_start()
GPIO.setmode(GPIO.BCM)
GPIO_PIR = 18
GPIO.setup(GPIO_PIR, GPIO.IN)
Current_State = 0
Previous_State = 0
try:
    while GPIO.input(GPIO_PIR) == 1:
        Current_State = 0
    while True:
        Current_State = GPIO.input(GPIO_PIR)
        if Current_State == 1 and Previous_State == 0:
            motion = {"motionDetected": True}
            client.publish("motion", json.dumps(motion))
            time.sleep(5)
            Previous_State = 1
        elif Current_State == 0 and Previous_State == 1:
            Previous_State = 0
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
