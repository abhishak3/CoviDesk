from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_env):
    app = Flask(__name__)
    app.config.from_object(config[config_env])
    
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    
    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
