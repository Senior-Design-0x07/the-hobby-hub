from flask_restful import Resource

class Connect_Wifi(Resource):
    def get(self):
        # subprocess.run([sys.executable, "/~/the-hobby-hub/scripts/scan_network.sh"])

    
    def post(self):
        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
