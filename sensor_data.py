import sys

sys.path.insert(0, "/home/pi/projects/raspberry-pi/lib")
import dht11
import json


def get_sensor_data(pin):
    instance = dht11.DHT11(pin)
    result = instance.read()

    if result.is_valid():
        data = {"temperature": result.temperature, "humidity": result.humidity}
        return json.dumps(data)
    else:
        error = {"error": {"type": "GetDataError", "description": "Unable to get data from sensor"}}
        return json.dumps(error)
