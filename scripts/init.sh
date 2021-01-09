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
echo -e "dev\ndev" | sudo passwd dev
