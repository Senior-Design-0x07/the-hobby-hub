#!/bin/sh

# Author : Anthony Bartman
# Description : This will install all neccessary files for
# our Flask backend server. Mostly from this tutorial: 
# https://www.codementor.io/@dongido/how-to-build-restful-apis-with-python-and-flask-12qto530jd

echo ""
echo "Copying web directory to /etc/hobby-hub "
echo ""

#Delete Pycache folders...
rm -r files/web/backend/__pycache__
rm -r files/web/backend/resources/__pycache__

#Copy directory to our folder on board
cp -r files/web /etc/hobby-hub/

