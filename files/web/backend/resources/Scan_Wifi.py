from flask_restful import Resource
import subprocess

class Scan_Wifi(Resource):
    def get(self):
        subprocess.run("/home/debian/the-hobby-hub/scripts/scan_network.sh")

        f = open("/home/debian/the-hobby-hub/files/wifi_scan/SSID.txt", "r")

        scanned_networks = f.readlines()

        f.close()
        return scanned_networks
    
    def post(self):
        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
