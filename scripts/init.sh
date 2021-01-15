#!/bin/sh

# Hobby Hub system configuration directory
mkdir -p /etc/hobby-hub/

# Startup script
cp files/init/start.sh /etc/hobby-hub/

# Program manager
mkdir -p /etc/hobby-hub/out/ # contains output of program manager
cp files/src/program_manager.py /etc/hobby-hub/ # program manager itself

# Pin mapping configuration
echo "{}" | sudo tee -a /etc/hobby-hub/pin_mapping.json # creates empty, but valid JSON file
