from .database import db
from flask import Flask
from flask_migrate import Migrate
from .config import config
from .models import Client, Room, Booking
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['database_uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']

    db.init_app(app)

    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main)

    return app
