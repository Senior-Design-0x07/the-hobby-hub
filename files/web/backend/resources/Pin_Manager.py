from flask_restful import Resource, reqparse
from flask import json

parser = reqparse.RequestParser()
parser.add_argument("ssid", type=str, help="Task is required DUDE.", required=True)
parser.add_argument("password", type=str, help="Task is required BRO.", required=True)

class Pin_Manager(Resource):

    def get(self):
        f = open("/etc/hobby-hub/pin_mapping.json", "r")
        pin_mapping = json.load(f)
        f.close()
        return pin_mapping
    def post(self):
        #For Andy
        args = parser.parse_args()

        print("REQUEST: ")
        print("   SSID: " + args["ssid"])
        print("   Password: " + args["password"])
        # Null in python
        return None
