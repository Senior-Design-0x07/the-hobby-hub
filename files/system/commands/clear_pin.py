import sys
import json
import argparse

PIN_MAP_FILE = "/etc/hobby-hub/pin_mapping.json"


def main(arguments):
    """API for clearing pins in the common JSON pin config file based on a program
    which is leaving the context.
    Methods:
    * clear_unused_pins(program_name)
    Args:
        arguments (list): list of arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('program_name',
                        help="program name associated with pins you want to clear")
    args = parser.parse_args(arguments)

    clear_unused_pins(args.program_name)


def clear_unused_pins(program_name):
    with open(PIN_MAP_FILE, 'r+') as f:
        pin_config = json.load(f)
        removed_pins = []
        for tag in pin_config:  # loop through each pin
            programs = pin_config[tag]["currently_used_programs"]
            running_programs = []
            for program in programs:  # loop though each program attached to the pin
                if program != program_name:
                    running_programs.append(program)
            if running_programs == []:  # if no programs need the pin, remove pin.
                removed_pins.append(tag)
            else:
                pin_config[tag]["currently_used_programs"] = running_programs
        for tag in removed_pins:
            pin_config.pop(tag)
        f.seek(0)
        json.dump(pin_config, f, indent=4)
        f.truncate()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
