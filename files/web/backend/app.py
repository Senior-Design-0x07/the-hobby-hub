from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.Pin_Manager import Pin_Manager
from resources.Program_Manager import Program_Manager
from resources.Scan_Wifi import Scan_Wifi

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(api_bp)

# Route
api.add_resource(Pin_Manager, '/pin_manager')
api.add_resource(Program_Manager, '/program_manager/<string:cmd>')
api.add_resource(Scan_Wifi, '/scan_wifi')
