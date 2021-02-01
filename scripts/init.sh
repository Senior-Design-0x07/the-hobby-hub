#!/bin/sh

# Hobby Hub system configuration directory
mkdir -p /etc/hobby-hub/

# Startup script
cp files/init/start.sh /etc/hobby-hub/

# Program manager
mkdir -p /etc/hobby-hub/out/ # contains output of program manager
chmod og=rw /etc/hobby-hub/out/
touch /etc/hobby-hub/out/paused_programs.txt
chmod og=rw /etc/hobby-hub/out/paused_programs.txt
touch /etc/hobby-hub/out/running_programs.txt
chmod og=rw /etc/hobby-hub/out/running_programs.txt
cp files/src/program_manager.py /etc/hobby-hub/ # program manager itself

# Hobby-hub command line utilitiy
cp files/src/hobby-hub /usr/bin/
