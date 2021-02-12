#!/bin/sh

sudo mkdir /etc/hobby-hub/cron
sudo rm -r /etc/crontab
sudo cp files/cron/crontab /etc/crontab
sudo cp files/cron/wif_scripts.sh /etc/hobby-hub/cron
