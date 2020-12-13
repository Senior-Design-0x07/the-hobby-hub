#!/bin/sh

# Author : Anthony Bartman
# Description : This will install all neccessary files for
# our Flask backend server. Mostly from this tutorial: 
# https://www.codementor.io/@dongido/how-to-build-restful-apis-with-python-and-flask-12qto530jd

echo ""
echo ""
echo "Running Flask Backend Install script."
echo "This may take a few moments..."
echo ""

#Use Python 3.7 on board, not using Python2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 7

#Install Pip (If Necessary)
sudo apt update
sudo apt install python3-pip
pip3 --version
echo " - Installed pip3"

#Install Virtual Env. to create isolated Python Env.
#WE DO NOT NEED A VIRTUAL ENVIRONMENT FOR OUR SENIOR DESIGN PROGRESS
# pip3 install virtualenv
# virtualenv --version
# echo " - Installed virtualenv"
# Create Virtual Environment
# python -m venv env
# echo " - Virtual Environment Created"

#Create Web Directory w/ base files(Front and Back end)
mkdir web && cd web && mkdir backend && mkdir frontend && cd backend && mkdir resources && mkdir templates
touch start.sh app.py run.py config.py requirements.txt && cd resources && touch Hello.py && cd ../ && cd templates && touch hello.html && cd ../
echo " - Web Directory and base files created"

#Installing other dependencies for Flask RESTful API
echo "flask==0.12.2 
flask_restful==0.3.6 
flask_script==2.0.6
marshmallow==2.14.0
flask_marshmallow==0.8.0" > requirements.txt
pip3 install -r requirements.txt
echo " - Dependencies Installed Globally"

#Setting up server files
echo "echo \" || STARTING SERVER ||\"

#Runs Server
python run.py" >> start.sh
chmod +rx start.sh
echo "import os

basedir = os.path.abspath(os.path.dirname(__file__))" > config.py
echo "from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')" > app.py
echo "from flask import Flask
from flask import render_template

def create_app(config_filename):
    app = Flask(__name__, static_url_path='', static_folder='../frontend')
    app.config.from_object(config_filename)

    @app.route('/')
    def index():
        return render_template('hello.html')

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == \"__main__\":
    app = create_app(\"config\")
    app.run(debug=True, host='0.0.0.0')" > run.py

cd resources
echo "from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {\"message\": \"Hello, World!\"}" > Hello.py
cd ../templates
echo "<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %} 
<button>Hi</button>" > hello.html
cd ../
echo " - Finished adding neccessary code to base files"

#Update user how to run server
echo ""
echo ""
echo "COMPLETED Flask Backend Install script."
echo "Read Below for use: "

echo "| Start Server: |"
echo " 1. Change directory to web/backend"
echo " 3a. Do 'pip3 install -r requirements.txt' the first time to install dependencies"
echo " 3b. Do './start.sh' to start server"
echo "| Stop Server: |"
echo " - CTRL + C in terminal"
echo "| Access server: |"
echo " - Open Chrome, and use http://192.168.7.2:5000 as URL"
echo " - Or use http://192.168.7.2:5000/api/Hello to view RESTful api data response"
echo " If IP does not work, try localhost:5000..."
echo " For some reason, localhost is quicker, and ip took me 1.2 minutes... rip for now"