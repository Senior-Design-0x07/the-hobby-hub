from flask_restful import Resource, reqparse
from flask import json
import subprocess, sys

class Pin_Manager(Resource):
    def get(self, cmd):
        if(cmd == 'grab_used_pins'):
            f = open("/etc/hobby-hub/pin_mapping.json", "r")
            pin_mapping = json.load(f)
            f.close()
            return pin_mapping
        elif(cmd == 'reset_config'):
            subprocess.call(['sudo','python3','/etc/hobby-hub/pin_manager.py','-x','/etc/hobby-hub/pin_mapping.json'])
            print('Reset')
            return None
        elif(cmd == 'clear_unused'):
            subprocess.call(['python3','/etc/hobby-hub/pin_manager.py','-x','/etc/hobby-hub/pin_mapping.json'])
            print('Cleared')
            return None        
