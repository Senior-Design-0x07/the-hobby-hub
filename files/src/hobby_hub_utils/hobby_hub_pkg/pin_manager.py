#!/usr/bin/env python3

import sys
import json
import argparse
import logging

class Pin:
    GPIO = 1
    PWM = 2
    I2C = 3
    ANALOG = 4
    SPECIAL = 5

PIN_MAP_FILE = "/etc/hobby-hub/pin_mapping.json"

# Table generated based on https://github.com/jadonk/bonescript/blob/master/src/bone.js
# (Adafruit_BBIO_NAME, Pin_Number)
pin_table = (
  ("USR0", 53, Pin.SPECIAL),
  ("USR1", 54, Pin.SPECIAL),
  ("USR2", 55, Pin.SPECIAL),
  ("USR3", 56, Pin.SPECIAL),
  #("DGND", 0),
  #("DGND", 0),
  ("GPIO1_6", 38, Pin.GPIO),
  ("GPIO1_7", 39, Pin.GPIO),
  ("GPIO1_2", 34, Pin.GPIO),
  ("GPIO1_3", 35, Pin.GPIO),
  ("TIMER4", 66, Pin.GPIO),
  ("TIMER7", 67, Pin.GPIO),
  ("TIMER5", 69, Pin.GPIO),
  ("TIMER6", 68, Pin.GPIO),
  ("GPIO1_13", 45, Pin.GPIO),
  ("GPIO1_12", 44, Pin.GPIO),
  ("EHRPWM2B", 23, Pin.PWM),
  ("GPIO0_26", 26, Pin.GPIO),
  ("GPIO1_15", 47, Pin.GPIO),
  ("GPIO1_14", 46, Pin.GPIO),
  ("GPIO0_27", 27, Pin.GPIO),
  ("GPIO2_1", 65, Pin.GPIO),
  ("EHRPWM2A", 22, Pin.PWM),
  ("GPIO1_30", 62, Pin.GPIO),
  ("GPIO1_5", 37, Pin.GPIO),
  ("GPIO1_4", 36, Pin.GPIO),
  ("GPIO1_31", 63, Pin.GPIO),
  ("GPIO1_1", 33, Pin.GPIO),
  ("GPIO1_0", 32, Pin.GPIO),
  ("GPIO1_29", 61, Pin.GPIO),
  ("GPIO2_22", 86, Pin.GPIO),
  ("GPIO2_24", 88, Pin.GPIO),
  ("GPIO2_23", 87, Pin.GPIO),
  ("GPIO2_25", 89, Pin.GPIO),
  ("UART5_CTSN", 10),
  ("UART5_RTSN", 11),
  ("UART4_RTSN", 9),
  ("UART3_RTSN", 81),
  ("UART4_CTSN", 8),
  ("UART3_CTSN", 80),
  ("UART5_TXD", 78),
  ("UART5_RXD", 79),
  ("GPIO2_12", 76, Pin.GPIO),
  ("GPIO2_13", 77, Pin.GPIO),
  ("GPIO2_10", 74, Pin.GPIO),
  ("GPIO2_11", 75, Pin.GPIO),
  ("GPIO2_8", 72, Pin.GPIO),
  ("GPIO2_9", 73, Pin.GPIO),
  ("GPIO2_6", 70, Pin.GPIO),
  ("GPIO2_7", 71, Pin.GPIO),
  #("DGND", 0),
  #("DGND", 0),
  #("VDD_3V3", 0),
  #("VDD_3V3", 0),
  #("VDD_5V", 0),
  #("VDD_5V", 0),
  #("SYS_5V", 0),
  #("SYS_5V", 0),
  #("PWR_BUT", 0),
  #("SYS_RESETn", 0),
  ("UART4_RXD", 30),
  ("GPIO1_28", 60, Pin.GPIO),
  ("UART4_TXD", 31),
  ("EHRPWM1A", 50, Pin.PWM),
  ("GPIO1_16", 48, Pin.GPIO),
  ("EHRPWM1B", 51, Pin.PWM),
  ("I2C1_SCL", 5),
  ("I2C1_SDA", 4),
  ("I2C2_SCL", 13, Pin.I2C),
  ("I2C2_SDA", 12, Pin.I2C),
  ("UART2_TXD", 3),
  ("UART2_RXD", 2),
  ("GPIO1_17", 49, Pin.GPIO),
  ("UART1_TXD", 15),
  ("GPIO3_21", 117, Pin.GPIO),
  ("UART1_RXD", 14),
  ("GPIO3_19", 115, Pin.GPIO),
  ("SPI1_CS0", 113),
  ("SPI1_D0", 111),
  ("SPI1_D1", 112),
  ("SPI1_SCLK", 110),
  #("VDD_ADC", 0),
  ("AIN4", 0, Pin.ANALOG),
  #("GNDA_ADC", 0),
  ("AIN6", 0, Pin.ANALOG),
  ("AIN5", 0, Pin.ANALOG),
  ("AIN2", 0, Pin.ANALOG),
  ("AIN3", 0, Pin.ANALOG),
  ("AIN0", 0, Pin.ANALOG),
  ("AIN1", 0, Pin.ANALOG),
  ("CLKOUT2", 20),
  ("GPIO0_7", 7, Pin.GPIO),
  #("DGND", 0),
  #("DGND", 0),
  #("DGND", 0),
  #("DGND", 0)
)




def main(arguments):
    """API for accessing the common pin mapping file

    This serves as the interface to access the common pin configuration JSON
    file.

    Methods:
    * request_pin(tag)
    * get_pin(tag)

    Args:
        arguments (list): list of arguments
    """

    logging.basicConfig(level=logging.INFO, )

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pin_config_filename',
                        help="JSON file containing the pin mapping file")

    parser.add_argument('-r', '--request-pin',
                        metavar='TAG',
                        help="Adds this tag to the pin mapping file")

    parser.add_argument('-g', '--get-pin',
                     metavar='TAG',
                     help="Return the value associated with the key in the json file.")

    parser.add_argument('-x', '--reset-config',
                        action='store_true',
                        help="Resets the pin configuration JSON file")

    parser.add_argument('-c', '--clear-unused',
                        action='store_true',
                        help="Identify and remove unused key-value pairs")

    args = parser.parse_args(arguments)

    logging.info(f'JSON file is {args.pin_config_filename}')

    if args.request_pin:
        request_pin(args.pin_config_filename, args.request_pin)

    if args.get_pin:
        value = get_pin(args.pin_config_filename, args.get_pin)
        if value is not None:
            print(f'The value associated with {args.get_pin} is {value}')
        else:
            print(f'No value associated with {args.get_pin} was found')

    if args.reset_config:
        reset(args.pin_config_filename)

    if args.clear_unused:
        clear_unused(args.pin_config_filename)


def request_pin(pin_config_filename, tag):
    """Adds the tag to the mapping file as a key-value pair

    The value (actual pin) will be dynamically changed by the web UI,
    so a placeholder value is added.

    If the tag already exists, there is no change.

    Args:
        tag (str): the tag to be the key in the config file
    """
    logging.info(f'Requesting pin {tag}')
    with open(pin_config_filename, 'r+') as f:
        pin_config = json.load(f)
        if tag in pin_config:
            logging.info(f'{tag} already in JSON file')
        else:
            pin_config[tag] = {}
            pin_config[tag]["pin"] = "P0"
            pin_config[tag]["in_use"] = False
            f.seek(0) # should reset file position to the beginning.
            json.dump(pin_config, f, indent=4)
            f.truncate() # remove remaining part
            logging.info(f'{tag} added to JSON with placeholder')


def get_pin(pin_config_filename, tag):
    """Return the value associated with the key in the json file.

    Args:
        tag (str): tag to search for

    Returns:
        str: value associated with tag
    """
    logging.info(f'Getting pin {tag}')
    value = None
    with open(pin_config_filename, 'r+') as f:
        pin_config = json.load(f)
        if tag in pin_config:
            value = pin_config[tag]
            logging.info(f'{tag}:{value} found in JSON file')
            pin_config[tag]["in_use"] = True
            f.seek(0) # should reset file position to the beginning.
            json.dump(pin_config, f, indent=4)
            f.truncate() # remove remaining part
            logging.info(f'{tag} marked as in use')

    return value


def reset(pin_config_filename):
    """Resets the pin configuration JSON file"""
    logging.info('Resetting config')
    with open(pin_config_filename, 'w') as f:
        f.write("{}")
        logging.info('Config reset')


def clear_unused(pin_config_filename):
    """Identify and remove unused key-value pairs

    Only the pins which are requested from the running programs should be available in the JSON file
    """
    logging.info('Clearing unused pins')
    with open(pin_config_filename, 'r+') as f:
        pin_config = json.load(f)
        unused_pins = [tag for tag in pin_config if pin_config[tag]["in_use"] == False]
        for tag in unused_pins:
            logging.info(f'Removing unused pin {tag}')
            del pin_config[tag]
        f.seek(0) # should reset file position to the beginning.
        json.dump(pin_config, f, indent=4)
        f.truncate() # remove remaining part
        logging.info('All unused pins cleared')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

def _get_pin(tag, type):
    with open(PIN_MAP_FILE, 'r+') as f:
        pin_config = json.load(f)
        physical_pin = ""
        if tag in pin_config:
            if pin_config[tag]["type"] == type:
                physical_pin = pin_config[tag]["pin"]
            else:
                raise KeyError("Requested pin " + tag + " of type: " + type + " already found as type: " + pin_config[tag]["type"])
        else:
            used_pins = []
            for tag_f in pin_config:
                used_pins.append(tag_f["pin"])
            for tag_d in pin_table:
                if (tag_d[0] not in used_pins) and (tag_d[2] == type):
                    pin_config[tag] = {}
                    pin_config[tag]["pin"] = tag_d[0]
                    pin_config[tag]["type" ] = type
                    physical_pin = tag_d[0]
                    break
            f.seek(0) # should reset file position to the beginning.
            json.dump(pin_config, f, indent=4)
            f.truncate() # remove remaining part
            logging.info(f'{tag} added to JSON with placeholder')
            return physical_pin


def get_gpio(tag):
    _get_pin(tag, Pin.GPIO)

