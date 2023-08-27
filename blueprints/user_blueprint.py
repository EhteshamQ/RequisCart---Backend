from flask import Flask, Blueprint

user_bluepint = Blueprint("users", __name__)


@user_bluepint.route('/users')