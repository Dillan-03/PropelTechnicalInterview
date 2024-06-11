from flask import Flask
from app.api.views import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.register_blueprint(api_blueprint)
    return app
