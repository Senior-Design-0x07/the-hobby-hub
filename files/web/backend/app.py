from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.Example import Example

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(api_bp)

# Route
api.add_resource(Example, '/Example')

