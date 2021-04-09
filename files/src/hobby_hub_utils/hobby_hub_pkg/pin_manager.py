#!/usr/bin/env python3

import sys
import json
import argparse
import logging

from .pin import Pin_t, Pin, Led

PIN_MAP_FILE = "/etc/hobby-hub/pin_mapping.json"
PIN_MANAGER_LOGGING_FILE = '/etc/hobby-hub/logs/pin_manager.log'

# Table generated based on https://github.com/jadonk/bonescript/blob/master/src/bone.js
# (Adafruit_BBIO_NAME, Pin_Number)
pin_table = (
  ("USR0", 53, Pin_t.SPECIAL),
  ("USR1", 54, Pin_t.SPECIAL),
  ("USR2", 55, Pin_t.SPECIAL),
  ("USR3", 56, Pin_t.SPECIAL),
  #("DGND", 0),
  #("DGND", 0),
  ("GPIO1_6", 38, Pin_t.GPIO),
  ("GPIO1_7", 39, Pin_t.GPIO),
  ("GPIO1_2", 34, Pin_t.GPIO),
  ("GPIO1_3", 35, Pin_t.GPIO),
  ("TIMER4", 66, Pin_t.GPIO),
  ("TIMER7", 67, Pin_t.GPIO),
  ("TIMER5", 69, Pin_t.GPIO),
  ("TIMER6", 68, Pin_t.GPIO),
  ("GPIO1_13", 45, Pin_t.GPIO),
  ("GPIO1_12", 44, Pin_t.GPIO),
  ("EHRPWM2B", 23, Pin_t.PWM),
  ("GPIO0_26", 26, Pin_t.GPIO),
  ("GPIO1_15", 47, Pin_t.GPIO),
  ("GPIO1_14", 46, Pin_t.GPIO),
  ("GPIO0_27", 27, Pin_t.GPIO),
  ("GPIO2_1", 65, Pin_t.GPIO),
  ("EHRPWM2A", 22, Pin_t.PWM),
  ("GPIO1_30", 62, Pin_t.GPIO),
  ("GPIO1_5", 37, Pin_t.GPIO),
  ("GPIO1_4", 36, Pin_t.GPIO),
  ("GPIO1_31", 63, Pin_t.GPIO),
  ("GPIO1_1", 33, Pin_t.GPIO),
  ("GPIO1_0", 32, Pin_t.GPIO),
  ("GPIO1_29", 61, Pin_t.GPIO),
  ("GPIO2_22", 86, Pin_t.GPIO),
  ("GPIO2_24", 88, Pin_t.GPIO),
  ("GPIO2_23", 87, Pin_t.GPIO),
  ("GPIO2_25", 89, Pin_t.GPIO),
  ("UART5_CTSN", 10),
  ("UART5_RTSN", 11),
  ("UART4_RTSN", 9),
  ("UART3_RTSN", 81),
  ("UART4_CTSN", 8),
  ("UART3_CTSN", 80),
  ("UART5_TXD", 78),
  ("UART5_RXD", 79),
  ("GPIO2_12", 76, Pin_t.GPIO),
  ("GPIO2_13", 77, Pin_t.GPIO),
  ("GPIO2_10", 74, Pin_t.GPIO),
  ("GPIO2_11", 75, Pin_t.GPIO),
  ("GPIO2_8", 72, Pin_t.GPIO),
  ("GPIO2_9", 73, Pin_t.GPIO),
  ("GPIO2_6", 70, Pin_t.GPIO),
  ("GPIO2_7", 71, Pin_t.GPIO),
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
  ("GPIO1_28", 60, Pin_t.GPIO),
  ("UART4_TXD", 31),
  ("EHRPWM1A", 50, Pin_t.PWM),
  ("GPIO1_16", 48, Pin_t.GPIO),
  ("EHRPWM1B", 51, Pin_t.PWM),
  ("I2C1_SCL", 5),
  ("I2C1_SDA", 4),
  ("I2C2_SCL", 13, Pin_t.I2C),
  ("I2C2_SDA", 12, Pin_t.I2C),
  ("UART2_TXD", 3),
  ("UART2_RXD", 2),
  ("GPIO1_17", 49, Pin_t.GPIO),
  ("UART1_TXD", 15),
  ("GPIO3_21", 117, Pin_t.GPIO),
  ("UART1_RXD", 14),
  ("GPIO3_19", 115, Pin_t.GPIO),
  ("SPI1_CS0", 113),
  ("SPI1_D0", 111),
  ("SPI1_D1", 112),
  ("SPI1_SCLK", 110),
  #("VDD_ADC", 0),
  ("AIN4", 0, Pin_t.ANALOG),
  #("GNDA_ADC", 0),
  ("AIN6", 0, Pin_t.ANALOG),
  ("AIN5", 0, Pin_t.ANALOG),
  ("AIN2", 0, Pin_t.ANALOG),
  ("AIN3", 0, Pin_t.ANALOG),
  ("AIN0", 0, Pin_t.ANALOG),
  ("AIN1", 0, Pin_t.ANALOG),
  ("CLKOUT2", 20),
  ("GPIO0_7", 7, Pin_t.GPIO),
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

    logging.basicConfig(level=logging.INFO, filename=PIN_MANAGER_LOGGING_FILE)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pin_config_filename',
                        help="JSON file containing the pin mapping file")

    parser.add_argument('-r', '--request-pin',
                        metavar=('TAG', 'TYPE'),
                        help="Adds this tag of specified type to the pin mapping file")

    parser.add_argument('-u', '--update-pin',
                        metavar=('TAG', 'PIN'),
                        help="Updates this tag to use the specified pin")

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
        tag, typ = args.update_pin
        request_pin(tag, typ)

    if args.update_pin:
        tag, pin = args.update_pin
        update_pin(args.pin_config_filename, tag, pin)

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


def update_pin(pin_config_filename, tag, pin):
    """Updates this tag to use the specified pin

    This method has no effect if the tag is not already managed or if the new pin is a different
    type.

    Args:
        tag (str): tag to update
        pin (str): new physical pin id

    Returns:
        True if pin was updated, False otherwise
    """
    logging.info(f'Updating pin {tag}')
    with open(pin_config_filename, 'r+') as f:
        pin_config = json.load(f)
        if tag not in pin_config:
            logging.info(f'Pin {tag} not found - not updating')
            return False
        for pin_tup in pin_table:
            if pin_tup[0] == pin:
                if pin_tup[2] != pin_config[tag]['type']:
                    logging.info(f'Pin {tag} is a different type - not updating')
                    return False
                else:
                    pin_config[tag]['pin'] = pin
                    f.seek(0) # should reset file position to the beginning.
                    json.dump(pin_config, f, indent=4)
                    f.truncate() # remove remaining part
                    logging.info(f'Pin {tag} updated to use {pin}')
                    return True

        logging.info(f'{pin} is not a valid pin')
        return False


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


def request_pin(tag, typ):
    with open(PIN_MAP_FILE, 'r+') as f:
        pin_config = json.load(f)
        physical_pin = ""
        if tag in pin_config:
            if pin_config[tag]["type"] == typ:
                physical_pin = pin_config[tag]["pin"]
            else:
                raise KeyError("Requested pin " + tag + " of type: " + type + " already found as type: " + pin_config[tag]["type"])
        else: # TODO fix this logic
            used_pins = []
            for config in pin_config.values():
                used_pins.append(config["pin"])
            for pin in pin_table:
                if (pin[0] not in used_pins) and (pin[2] == typ):
                    pin_config[tag] = {}
                    pin_config[tag]["pin"] = pin[0]
                    pin_config[tag]["type" ] = typ
                    physical_pin = pin[0]
                    break
            f.seek(0) # should reset file position to the beginning.
            json.dump(pin_config, f, indent=4)
            f.truncate() # remove remaining part
            logging.info(f'{tag} added to JSON with placeholder')

        return physical_pin


def get_gpio(tag):
    return Pin(request_pin(tag, Pin_t.GPIO))


def get_led(tag):
    return Led(request_pin(tag, Pin_t.SPECIAL))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
