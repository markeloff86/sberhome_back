import RPi.GPIO as GPIO


def is_motioned(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    GPIO.wait_for_edge(pin, GPIO.RISING, 200)
    result = GPIO.input(pin)
    return result

