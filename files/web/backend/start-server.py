from flask import Flask,redirect
from flask_cors import CORS
# from flask_talisman import Talisman
from app import api_bp

def create_app(config_filename):
    app = Flask(__name__, static_url_path='',static_folder='../frontend')
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='/api')
    # Talisman(app)

    @app.route('/')
    def index():
        return redirect('http://192.168.7.2:5000/index.html')

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0', ssl_context=('certificates/server.crt','certificates/server.key'))
