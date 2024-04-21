from flask import Flask
from flask_migrate import Migrate

from config import Config
from db import db
from .routes import register_blueprints
from .auth import init_auth
from .utils import cache

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.static_folder = "static"

    cache.init_app(app)
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all()

    register_blueprints(app)
    init_auth(app)

    return app
