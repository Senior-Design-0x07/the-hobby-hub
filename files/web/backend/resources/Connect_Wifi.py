from flask_restful import Resource, reqparse
from flask import json
import os
import subprocess

parser = reqparse.RequestParser()
parser.add_argument("ssid", type=str, help="Task is required DUDE.", required=True)
parser.add_argument("password", type=str, help="Task is required BRO.", required=True)

class Connect_Wifi(Resource):
    def get(self):
        return null

    
    def post(self):
        args = parser.parse_args()
        command = "sudo wpa_passphrase " + args["ssid"] + " " + args["password"] + " | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
        os.system(command)
        subprocess.run("/home/debian/the-hobby-hub/files/cron/wifi_scripts.sh")


        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
