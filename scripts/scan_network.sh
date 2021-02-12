#!/bin/sh

sudo touch files/wifi_scan/SSID.txt
sudo /sbin/iw wlan0 scan | grep SSID > files/wifi_scan/SSID.txt
