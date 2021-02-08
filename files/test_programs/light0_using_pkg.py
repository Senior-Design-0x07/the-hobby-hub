from hobby_hub_pkg.pin_manager import get_led
from time import sleep

led = get_led("myled0")
iters = 10
delay = 1

for _ in range(iters):
    led.turn_on()
    sleep(delay)

    led.turn_off()
    sleep(delay)