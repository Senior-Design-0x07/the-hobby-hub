#!/bin/sh

# This program provides a script that is run upon device startup that will
# act as an entry point to startup the rest of the hobby-hub utilities (as needed).

# test message - viewable in $journalctl

# Start program manager
sudo python3 /etc/hobby-hub/program_manager.py /etc/hobby-hub/test_programs/ > /etc/hobby-hub/out/running_programs.txt

echo "hobby-hub startup sucessful!"
