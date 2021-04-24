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
            clear_unused("/etc/hobby-hub/pin_mapping.json")
            return True 
        elif(cmd == 'reset_config'):
            reset("/etc/hobby-hub/pin_mapping.json")
            return True
    def post(self, cmd):
        if(cmd == 'request_pin'):
            args = requestPinParser.parse_args()
            try:
                physical_pin = request_pin(args["pin_name"],int(args["pin_type"]))
                return True
            except:
                return False
        elif(cmd == 'get_pin'):
            args = getPinParser.parse_args()
            return get_pin("/etc/hobby-hub/pin_mapping.json", args["pin_name"])
        elif(cmd == 'update_pin'):
            args = updatePinParser.parse_args()
            return update_pin("/etc/hobby-hub/pin_mapping.json",args["pin_name"],args["new_physical_pin"])
