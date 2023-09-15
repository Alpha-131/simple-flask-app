from flask import Flask
from flask_app.config import config

def create_app(config_class=config):
    app = Flask(__name__)

    app.config.from_object(config)

    from flask_app.main.routes import main
    from flask_app.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app