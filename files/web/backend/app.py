from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.Pin_Manager import Pin_Manager
from resources.Program_Manager import Program_Manager
from resources.Wifi_Requests import Wifi_Requests
from resources.Logging import Logging

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(api_bp)

# Route
api.add_resource(Program_Manager, '/program_manager/<string:cmd>')
api.add_resource(Wifi_Requests, '/wifi_request/<string:cmd>')
api.add_resource(Pin_Manager, '/pin_manager/<string:cmd>')
api.add_resource(Logging, '/logging/<string:cmd>')
