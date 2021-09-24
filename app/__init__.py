from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_env):
    app = Flask(__name__)
    app.config.from_object(config[config_env])
    
    db.init_app(app)
    
    from .main import main
    app.register_blueprint(main)

    return app
