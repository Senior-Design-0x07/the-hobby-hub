from hobby_hub_pkg.pin_manager import get_led
from time import sleep

led = get_led("myled0")
delay = 1

while True:
    led.turn_on()
    sleep(delay)

    led.turn_off()
    sleep(delay)
