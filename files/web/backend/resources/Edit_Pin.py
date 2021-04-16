from flask_restful import Resource, reqparse
from flask import json
import subprocess, sys
from subprocess import Popen, PIPE

from hobby_hub_pkg.pin_manager import update_pin,get_pin,request_pin

# parser = reqparse.RequestParser()
# parser.add_argument("ssid", type=str, help="Task is required DUDE.", required=True)
# parser.add_argument("password", type=str, help="Task is required BRO.", required=True)
# args = parser.parse_args()
# print("REQUEST: ")
# print("   SSID: " + args["ssid"])
# print("   Password: " + args["password"])

class Edit_Pin(Resource):

    def get(self, cmd, pin_name,typ):
        if(cmd == 'request_pin'):
            # ** THIS METHOD grabs the number of pins that use the type you search for **
            # cmdResult = subprocess.Popen(['sudo','python3','/etc/hobby-hub/pin_manager.py', '-r', pin_name, '/etc/hobby-hub/pin_mapping.json'], stdout=subprocess.PIPE)
            # tuple1 = cmdResult.communicate()[0]
            # string_dict = tuple1.decode("utf-8")
            string_dict = request_pin(pin_name,typ)
            print("BLAH: " + string_dict)
            # pin = json.loads(string_dict)
            return 'true' if True else False
        elif(cmd == 'get_pin'):
            foundPin = get_pin("/etc/hobby-hub/pin_mapping.json", pin_name)
            return foundPin
