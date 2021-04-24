import Adafruit_BBIO.GPIO as GPIO


class Pin_t:
    GPIO = 1
    PWM = 2
    I2C = 3
    ANALOG = 4
    SPECIAL = 5
    UART = 6
    SPI = 7


class Pin:

    def __init__(self, name):
        self.name = name
        self.high = False
        GPIO.setup(name, GPIO.OUT)

    def set_high(self):
        if self.high is False:
            GPIO.output(self.name, GPIO.HIGH)
            self.high = True

    def set_low(self):
        if self.high is True:
            GPIO.output(self.name, GPIO.LOW)
            self.high = False


class Led(Pin):

    def turn_on(self):
        self.set_high()

    def turn_off(self):
        self.set_low()

