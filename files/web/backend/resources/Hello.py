from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {"greetings": "Hello From Flask in Hello.py"}
