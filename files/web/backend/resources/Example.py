from flask_restful import Resource

class Example(Resource):
    def get(self):
        return {"num_backend": 5,"string_backend": "Hello From Flask in Example.py"}
