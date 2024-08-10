from flask import Flask
from .routes import main_blueprint
from .utils.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register Blueprints
    app.register_blueprint(main_blueprint)

    return app
