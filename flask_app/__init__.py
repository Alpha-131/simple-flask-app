from flask import Flask
from flask_app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=config):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from flask_app.main.routes import main
    from flask_app.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app  