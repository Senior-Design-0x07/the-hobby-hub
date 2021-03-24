#!/bin/sh

sudo /sbin/iw wlan0 scan | grep SSID > /home/debian/the-hobby-hub/files/wifi_scan/SSID.txt
