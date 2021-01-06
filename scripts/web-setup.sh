#!/bin/sh

# Author : Anthony Bartman
# Description : This will install all neccessary files for
# our web Flask Backend and Flutter Frontend to our folder on board

echo ""
echo "Copying web directory to /etc/hobby-hub "
echo ""

#Delete Pycache folders...
rm -r files/web/backend/__pycache__
rm -r files/web/backend/resources/__pycache__

#Copy directory to our folder on board
cp -r files/web /etc/hobby-hub/

