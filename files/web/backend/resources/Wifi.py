from flask_restful import Resource

class Wifi(Resource):
    def get(self):
        return {"message": "Hello, World!"}
