#!/bin/sh

# This program provides a script that is run upon device startup that will
# act as an entry point to startup the rest of the hobby-hub utilities (as needed).

#Runs Flask Backend Server on startup
echo " || Starting Web Server ||"
python /etc/hobby-hub/web/backend/start-server.py

# test message - viewable in $journalctl
echo "hobby-hub startup sucessful!"
