#!/bin/sh

# Author : Anthony Bartman
# Description : This will install all neccessary dependencies for
# our Flask backend server. Mostly from this tutorial: 
# https://www.codementor.io/@dongido/how-to-build-restful-apis-with-python-and-flask-12qto530jd

echo ""
echo ""
echo "Installing Python Dependencies..."
echo "This may take a few moments..."
echo ""

#Use Python 3.7 on board, not using Python2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 7

#Install Pip (If Necessary)
sudo apt install python3-pip
pip3 --version
echo " - Installed pip3"

#Flask RESTful backend dependencies
pip3 install flask==0.12.2
pip3 install flask_restful==0.3.6
pip3 install flask_script==2.0.6
pip3 install marshmallow==2.14.0
pip3 install flask_marshmallow==0.8.0
pip3 install -U flask-cors
echo " - Installed Python dependencies"

#Install Virtual Env. to create isolated Python Env.
#WE DO NOT NEED A VIRTUAL ENVIRONMENT FOR OUR SENIOR DESIGN PROGRESS
# pip3 install virtualenv
# virtualenv --version
# echo " - Installed virtualenv"
# Create Virtual Environment
# python -m venv env
# echo " - Virtual Environment Created"

#Update user how to run server
echo "COMPLETED Flask Backend Install script."

