#!/bin/sh

sudo wpa_passphrase $1 $2 | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf