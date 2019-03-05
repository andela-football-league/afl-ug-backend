import os

from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config.get(config_name, 'default'))

    # import blueprints
    from home.views import home

    # register blueprints
    app.register_blueprint(home)

    return app
