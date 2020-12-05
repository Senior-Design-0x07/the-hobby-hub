#!/bin/sh

cp files/systemd/service/hobby_hub_entry.service /etc/systemd/system
#ln -s /lib/systemd/system/hobby_hub_entry.service /etc/systemd/system/multi-user.target.wants/hobby_hub_entry.service
