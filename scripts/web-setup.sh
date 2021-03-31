#!/bin/sh

# Author : Anthony Bartman
# Description : This will install all neccessary files for
# our Flask backend server. Mostly from this tutorial: 
# https://www.codementor.io/@dongido/how-to-build-restful-apis-with-python-and-flask-12qto530jd

echo "Installing web server."

rm -r /etc/hobby-hub/web/backend/__pycache__
rm -r /etc/hobby-hub/web/backend/resources/__pycache__
rm /etc/apt/sources.list.d/sources.list

#Copy directory to our folder on board
cp -r files/web /etc/hobby-hub/

echo "Web server installed!"

