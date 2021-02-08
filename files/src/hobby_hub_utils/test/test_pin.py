from hobby_hub_pkg.pin_manager import get_led
import unittest
import time

class TestStringMethods(unittest.TestCase):

    def test_blink_led0(self):
        led = get_led("myled0")
        iters = 10
        delay = 1

        for _ in range(iters):
            led.turn_on()
            time.sleep(delay)

            led.turn_off()
            time.sleep(delay)

if __name__ == '__main__':
    unittest.main()
