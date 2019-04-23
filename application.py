from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config.get(config_name, "default"))

    # setup_db
    db.init_app(app)

    # Return validation errors as JSON
    @app.errorhandler(422)
    @app.errorhandler(400)
    def handle_error(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    # import blueprints
    from home.views import home
    from api.person.views import person_app
    from api.team.views import team_app
    from api.permissions import permission_app

    # register blueprints
    app.register_blueprint(home)
    app.register_blueprint(team_app)
    app.register_blueprint(person_app)
    app.register_blueprint(permission_app)

    return app
