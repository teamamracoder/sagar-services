from flask import Flask
from flask_migrate import Migrate

from config import Config
from db import db
from .routes import register_blueprints
from .auth import init_auth
from .controllers.auth_controller import init_cache


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.static_folder = "static"

    init_cache(app)
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all()

    register_blueprints(app)
    init_auth(app)

    return app
