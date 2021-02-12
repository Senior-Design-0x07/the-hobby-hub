#!/bin/sh

# Author : Anthony Bartman
# Description : This will install all neccessary files for
# our web Flask Backend and Flutter Frontend to our folder on board

echo ""
echo "Copying web directory to /etc/hobby-hub "
echo ""

#Delete Pycache folders
rm -r files/web/backend/__pycache__
rm -r files/web/backend/resources/__pycache__
rm /etc/apt/sources.list.d/sources.list

# #Install dependencies for https certificates and all
# # https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https 
# #Generates 2 keys, need to determine how to input parameters in cmd line with this xD
# cd files/web/backend
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
# apt-get install software-properties-common
# #Create sources list with stretch-backports
# cd /etc/apt/sources.list.days

#Copy directory to our folder on board
cp -r files/web /etc/hobby-hub/

echo "Web server installed!"

