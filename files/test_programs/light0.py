import Adafruit_BBIO.GPIO as GPIO
import time

USR0_LED = "USR0"
delay = 0.5
GPIO.setup(USR0_LED, GPIO.OUT)

while (True):
    GPIO.output(USR0_LED, GPIO.HIGH)
    time.sleep(delay)

    GPIO.output(USR0_LED, GPIO.LOW)
    time.sleep(delay)
