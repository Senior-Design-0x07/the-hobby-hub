from flask_restful import Resource, reqparse
from flask import json
import subprocess, sys
from hobby_hub_pkg.pin_manager import reset,clear_unused,update_pin,get_pin,request_pin,pin_table

#Request_pin (ie Creates new pin) parser
requestPinParser = reqparse.RequestParser()
requestPinParser.add_argument("pin_name", type=str, help="Need pin_name for new pin", required=True)
requestPinParser.add_argument("pin_type", type=str, help="Need pin_type for new pin", required=True)
#Get_pin (ie Validate pin is in list) parser
getPinParser = reqparse.RequestParser()
getPinParser.add_argument("pin_name", type=str, help="Need pin_name for finding a pin", required=True)
#Update_pin (ie Change name of pin) parser
updatePinParser = reqparse.RequestParser()
updatePinParser.add_argument("pin_name", type=str, help="Need pin_name for updating a pin", required=True)
updatePinParser.add_argument("new_physical_pin", type=str, help="Need new_physical_pin for updating a pin", required=True)

class Pin_Manager(Resource):
    def get(self, cmd):
        if(cmd == 'grab_used_pins'):
            f = open("/etc/hobby-hub/pin_mapping.json", "r")
            pin_mapping = json.load(f)
            f.close()
            return pin_mapping
        elif(cmd == "grab_physical_pins"):
            return pin_table
        elif(cmd == 'clear_unused'):
            # subprocess.call(['sudo','python3','/etc/hobby-hub/pin_manager.py','-c','/etc/hobby-hub/pin_mapping.json'])
            clear_unused("/etc/hobby-hub/pin_mapping.json")
            return 'false' if True else False 
        elif(cmd == 'reset_config'):
            reset("/etc/hobby-hub/pin_mapping.json")
            return 'true' if True else False
    def post(self, cmd):
        if(cmd == 'request_pin'):
            # ** THIS METHOD grabs the number of pins that use the type you search for **
            # cmdResult = subprocess.Popen(['sudo','python3','/etc/hobby-hub/pin_manager.py', '-r', pin_name, '/etc/hobby-hub/pin_mapping.json'], stdout=subprocess.PIPE)
            # tuple1 = cmdResult.communicate()[0]
            # string_dict = tuple1.decode("utf-8")
            args = requestPinParser.parse_args()
            string_dict = request_pin(args["pin_name"],int(args["pin_type"]))
            print("BLAH: " + string_dict)
            # pin = json.loads(string_dict)
            return 'true' if True else False
        elif(cmd == 'get_pin'):
            args = getPinParser.parse_args()
            foundPin = get_pin("/etc/hobby-hub/pin_mapping.json", args["pin_name"])
            return foundPin
        elif(cmd == 'update_pin'):
            args = updatePinParser.parse_args()
            didItWork = update_pin("/etc/hobby-hub/pin_mapping.json",args["pin_name"],args["new_physical_pin"])
            return didItWork
