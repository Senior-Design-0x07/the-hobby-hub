#!/bin/sh

# Hobby Hub system configuration directory
mkdir -p /etc/hobby-hub/

# Startup script
cp files/init/start.sh /etc/hobby-hub/

# Program manager
mkdir -p /etc/hobby-hub/out/ # contains output of program manager
cp files/src/program_manager.py /etc/hobby-hub/ # program manager itself

# Create dev user & group. add new user to required groups.
sudo useradd --comment "Development User" --user-group --create-home --shell /bin/bash dev
sudo usermod --append --groups dev debian
sudo usermod --append --groups dialout,users,systemd-journal,bluetooth,i2c,gpio,pwm,spi,iio dev
sleep 1
echo 'dev:dev' | sudo chpasswd

# Update SSH connection interface
sudo cp files/system/motd /etc/
sudo cp files/system/sshd_config /etc/ssh/
sudo cp files/system/issue.net /etc/

# Pin mapping configuration
echo "{}" | sudo tee -a /etc/hobby-hub/pin_mapping.json # creates empty, but valid JSON file
chmod og=rw /etc/hobby-hub/pin_mapping.json
# cp files/src/hobby_hub_utils/hobby_hub_pkg/pin_manager.py /etc/hobby-hub/ # pin manager itself
sudo python3 -m pip install /home/debian/the-hobby-hub/files/src/hobby_hub_utils # install package for user dev
