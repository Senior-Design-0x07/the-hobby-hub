#!/usr/bin/env python3

import sys
import json
import argparse
import logging

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
            pin_config[tag] = "P0"
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
    with open(pin_config_filename, 'r') as f:
        pin_config = json.load(f)
        if tag in pin_config:
            value = pin_config[tag]
            logging.info(f'{tag}:{value} found in JSON file')

    return value


def reset(pin_config_filename):
    """Resets the pin configuration JSON file"""
    logging.info('Resetting config')
    with open(pin_config_filename, 'w') as f:
        f.write("{}")
        logging.info('Config reset')


def clear_unused():
    """Identify and remove unused key-value pairs

    Only the pins which are requested from the running programs should be available in the JSON file
    """
    pass


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))