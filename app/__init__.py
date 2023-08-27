from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from alembic import context
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from models import user, base, cart, image, item, payment, order  # noqa : E402 , F401


config = context.config if hasattr(context, "config") else None

target_metadata = base.Base.metadata

from blueprints.user import user_bluepint  # noqa : E402

app.register_blueprint(user_bluepint)

# setting up logging in a different file to not clutter the console
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "DEBUG").upper(),
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)
