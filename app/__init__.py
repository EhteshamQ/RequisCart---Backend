from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from alembic import context
from dotenv import load_dotenv

load_dotenv()

print(os.environ["APP_SETTINGS"])
app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from models import user, base, cart, image, item, payment, order


config = context.config

target_metadata = base.Base.metadata
