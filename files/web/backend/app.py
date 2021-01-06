from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.Hello import Hello

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(api_bp)

# Route
api.add_resource(Hello, '/Hello')

