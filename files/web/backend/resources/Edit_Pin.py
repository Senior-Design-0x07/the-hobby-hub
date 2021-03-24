from flask_restful import Resource, reqparse
from flask import json
import subprocess, sys
from subprocess import Popen, PIPE

parser = reqparse.RequestParser()
parser.add_argument("ssid", type=str, help="Task is required DUDE.", required=True)
parser.add_argument("password", type=str, help="Task is required BRO.", required=True)

class Edit_Pin(Resource):

    def get(self, cmd, pin_name):
        if(cmd == 'get_pin'):
            cmdResult = subprocess.Popen(['sudo','python3','/etc/hobby-hub/pin_manager.py', '-g', pin_name, '/etc/hobby-hub/pin_mapping.json'], stdout=subprocess.PIPE)
            tuple1 = cmdResult.communicate()[0]
            string_dict = tuple1.decode("utf-8")\
                                .replace('\'','\"')\
                                .replace('T','t')\
                                .split(" ", 6)[6]
            #Convert dictionary string to dictionary
            pin = json.loads(string_dict) 
            return pin
    def post(self, cmd):
        print(cmd)
        if(cmd == 'request_pin'):
            args = parser.parse_args()

            print("REQUEST: ")
            print("   SSID: " + args["ssid"])
            print("   Password: " + args["password"])
            # Null in python
            return None
