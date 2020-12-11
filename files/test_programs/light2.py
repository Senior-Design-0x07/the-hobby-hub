import Adafruit_BBIO.GPIO as GPIO
import time

USR1_LED = "USR2"
delay = 0.25
GPIO.setup(USR1_LED, GPIO.OUT)

while (True):
    GPIO.output(USR1_LED, GPIO.HIGH)
    time.sleep(delay)

    GPIO.output(USR1_LED, GPIO.LOW)
    time.sleep(delay)
