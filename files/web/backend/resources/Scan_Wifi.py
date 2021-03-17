from flask_restful import Resource
from flask import json

class Scan_Wifi(Resource):
    def get(self):
        # subprocess.run([sys.executable, "/~/the-hobby-hub/scripts/scan_network.sh"])

        f = open("/home/debian/the-hobby-hub/files/wifi_scan/SSID.json", "r")
        scanned_networks = json.load(f)
        f.close()
        return scanned_networks
    def post(self):
        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
