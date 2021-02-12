import Adafruit_BBIO.GPIO as GPIO
import time

USR2_LED = "USR2"
delay = 0.25
GPIO.setup(USR2_LED, GPIO.OUT)

while (True):
    GPIO.output(USR2_LED, GPIO.HIGH)
    time.sleep(delay)

    GPIO.output(USR2_LED, GPIO.LOW)
    time.sleep(delay)
