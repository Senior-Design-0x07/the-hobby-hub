from flask_restful import Resource, reqparse
from flask import json
import os
import subprocess

parser = reqparse.RequestParser()
parser.add_argument("ssid", type=str, help="Task is required DUDE.", required=True)
parser.add_argument("password", type=str, help="Task is required BRO.", required=True)

class Wifi_Requests(Resource):
    def get(self):
        os.system("sudo /sbin/iw wlan0 scan | grep SSID > /etc/hobby-hub/wifi_scan/SSID.txt")
        scanned_networks = []
        parsed_networks = []

        f = open("/etc/hobby-hub/wifi_scan/SSID.txt", "r")
        scanned_networks = f.readlines()
        f.close()

        for line in scanned_networks:
            parsed_networks.append(line.strip())
         
        return str(parsed_networks)[1:-1]
    
    def post(self):
        args = parser.parse_args()
        command = "sudo wpa_passphrase " + args["ssid"] + " " + args["password"] + " | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
        os.system(command)
        subprocess.run("/etc/hobby-hub/cron/wifi_scripts.sh")

        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
