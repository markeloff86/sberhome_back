import time

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import sensor_data


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

# client.username_pw_set("mqtt_client", "pass")
client.connect("18.223.169.60", 1883, 60)
client.loop_start()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

try:
    while True:
        client.publish("sensor_data", sensor_data.get_sensor_data(14))
        time.sleep(10)
except KeyboardInterrupt:
    print("Quit")
    # Reset GPIO settings
    GPIO.cleanup()
