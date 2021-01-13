#!/usr/bin/env python3

import sys


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
    pass


def request_pin(tag):
    """Adds the tag to the mapping file as a key-value pair

    The value (actual pin) will be dynamically changed by the web UI,
    so a placeholder value is added.

    If the tag already exists, there is no change.

    Args:
        tag (str): the tag to be the key in the config file
    """
    pass


def get_pin(tag):
    """Return the value associated with the key in the json file.

    Args:
        tag (str): tag to search for

    Returns:
        str: value associated with tag
    """
    return ""


def reset():
    """Resets the pin configuration JSON file"""
    pass


def clear_unused():
    """Identify and remove unused key-value pairs

    Only the pins which are requested from the running programs should be available in the JSON file
    """


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))