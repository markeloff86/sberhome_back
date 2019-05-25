import sys

sys.path.insert(0, "/home/pi/projects/raspberry-pi/lib")
import dht11
import json


def get_humidity_status(value):
    if 40 <= value <= 60:
        print("DEBUG_HUMIDITY_comfortable: %s", value)
        return "comfortable"
    elif value < 40:
        print("DEBUG_HUMIDITY_low: %s", value)
        return "low"
    else:
        print("DEBUG_HUMIDITY_high %s", value)
        return "high"


def get_temperature_status(value):
    if 21 <= value <= 26:
        print("DEBUG_TEMP_comfortable %s", value)
        return "comfortable"
    elif value < 21:
        print("DEBUG_TEMP_low %s", value)
        return "low"
    else:
        print("DEBUG_TEMP_high %s", value)
        return "high"


def get_sensor_data(pin):
    instance = dht11.DHT11(pin)
    result = instance.read()

    if result.is_valid():
        data = {"temperature":
                    {"value": result.temperature, "status": get_temperature_status(result.temperature)},
                "humidity":
                    {"value": result.humidity, "status": get_humidity_status(result.humidity)}
                }
        return json.dumps(data)
    else:
        error = {"error": {"type": "GetDataError", "description": "Unable to get data from sensor"}}
        return json.dumps(error)
