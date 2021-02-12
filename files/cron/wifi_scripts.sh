#!/bin/sh

sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -D nl80211 
sudo dhclient wlan0 
sleep 10
