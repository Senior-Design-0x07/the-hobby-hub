#!/bin/sh

# Hobby Hub system configuration directory
mkdir -p /etc/hobby-hub/

# Startup script
cp files/init/start.sh /etc/hobby-hub/

# Program manager
mkdir -p /etc/hobby-hub/out/ # contains output of program manager
touch /etc/hobby-hub/out/paused_programs.txt
cp files/src/program_manager.py /etc/hobby-hub/ # program manager itself
