from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.Pin_Manager import Pin_Manager
from resources.Wifi_Requests import Wifi_Requests
from resources.Edit_Pin import Edit_Pin
from resources.Logging import Logging

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(api_bp)

# Route
api.add_resource(Pin_Manager, '/pin_manager')
api.add_resource(Wifi_Requests, '/wifi_request/<string:cmd>')
api.add_resource(Pin_Manager, '/pin_manager/<string:cmd>')
api.add_resource(Edit_Pin, '/pins/<string:cmd>/<string:pin_name>/<int:typ>')