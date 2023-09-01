import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from alembic import context

load_dotenv()


db = SQLAlchemy()

from models import base, cart, image, item, order, payment, user  # noqa : E402 , F401

config = context.config if hasattr(context, "config") else None
target_metadata = base.Base.metadata


from blueprints.user import user_bluepint  # noqa : E402

# setting up logging in a different file to not clutter the console
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "DEBUG").upper(),
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def init_app():
    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    app.register_blueprint(user_bluepint)
    return app
