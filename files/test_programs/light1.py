import Adafruit_BBIO.GPIO as GPIO
import time

USR1_LED = "USR1"
delay = 0.5
GPIO.setup(USR1_LED, GPIO.OUT)

while (True):
    GPIO.output(USR1_LED, GPIO.HIGH)
    time.sleep(delay)

    GPIO.output(USR1_LED, GPIO.LOW)
    time.sleep(delay)