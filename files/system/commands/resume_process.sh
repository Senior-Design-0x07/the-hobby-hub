#!bin/sh
/usr/bin/kill $(ps aux | grep 'target_application' | awk '{print $2}')
