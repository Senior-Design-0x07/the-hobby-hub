#!/bin/sh

sudo mkdir /etc/hobby-hub/cron

echo "sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -D nl80211 \nsudo dhclient wlan0 \nsleep 10" | sudo tee /etc/hobby-hub/cron/wifi_scripts.sh

sudo rm -r /etc/crontab
sudo cp files/cron/crontab /etc/crontab
