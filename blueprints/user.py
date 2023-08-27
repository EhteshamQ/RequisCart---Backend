from flask import Blueprint, request
import json
from models.user import User
from uuid import UUID
from response_entities.user import UserResponse
import logging

user_bluepint = Blueprint("users", __name__)


@user_bluepint.route("/users", methods=["GET"])
def get_all_users():
    try:
        users: list = User.query.all()
        user_models = list(map(lambda user: UserResponse(user), users))
        return json.dumps(user_models), 200

    except Exception as e:
        logging.exception(f"Exception - {e}")
        return "There was an error with the request", 500


@user_bluepint.route("/users/<string:user_id>", methods=["GET"])
def get_user_by_id(user_id: str):
    try:
        user = User.query.get(UUID(user_id))
        if user is None:
            return "No User with this user id", 404
        return UserResponse(user), 200
    except Exception as e:
        logging.exception(f"Exception - {e}")
        return 500


@user_bluepint.route("/users", methods=["POST"])
def create_user():
    # user_request = request.get_json()
    # TODO: Complete this Check the Request object first, then Check if it exists in db, if yes,
    # Figure out what to do, else push record to db & create a new mail to send mails to users,
    # complete the registration process & send 200 response , on Successful activation create a cart for the user
    # Add Authentication & JWT logic
    return "Failed to create user", 500
