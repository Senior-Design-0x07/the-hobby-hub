from flask import Flask
from flask import render_template

def create_app(config_filename):
    app = Flask(__name__, static_url_path='',static_folder='../frontend')
    app.config.from_object(config_filename)

    @app.route('/')
    def index():
        return render_template('hello.html')

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True, host='0.0.0.0')
