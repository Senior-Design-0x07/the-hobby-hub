import Adafruit_BBIO.GPIO as GPIO
import time

USR3_LED = "USR3"
delay = 0.125
GPIO.setup(USR3_LED, GPIO.OUT)

while (True):
    GPIO.output(USR3_LED, GPIO.HIGH)
    time.sleep(delay)

    GPIO.output(USR3_LED, GPIO.LOW)
    time.sleep(delay)
