from flask_restful import Resource
from flask import json

class Pin_Manager(Resource):
    def get(self):
        f = open("/etc/hobby-hub/pin_mapping.json", "r")
        pin_mapping = json.load(f)
        f.close()
        return pin_mapping
    def post(self):
        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
