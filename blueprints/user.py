import json
from typing import Optional
from flask import Blueprint, request
from marshmallow import ValidationError
from models.user import User
from uuid import UUID
from request_dtos.user_request import UserRequest
from schemas.user import UserSchema
import logging
from app import db


user_bluepint = Blueprint("users", __name__)


@user_bluepint.route("/users", methods=["GET"])
def get_all_users():
    try:
        users: list[User] = User.query.all()
        user_models = list(map(lambda user: user.to_dict(), users))
        return UserSchema(many=True).dumps(user_models), 200

    except Exception as e:
        logging.exception(f"Exception - {e}")
        return "There was an error with the request", 500


@user_bluepint.route("/users/<string:user_id>", methods=["GET"])
def get_user_by_id(user_id: str):
    try:
        user: Optional[User] = User.query.get(UUID(user_id))
        if user is None:
            return "No User with this user id", 404
        return UserSchema().dumps(user.to_dict()), 200
    except Exception as e:
        logging.exception(f"Exception - {e}")
        return 500


@user_bluepint.route("/users", methods=["POST"])
def create_user():
    # TODO: Complete this Check the Request object first, then Check if it exists in db, if yes,
    # Figure out what to do, else push record to db & create a new mail to send mails to users,
    # complete the registration process & send 200 response , on Successful activation create a cart for the user
    # Add Authentication & JWT logic

    try:
        user_schema = UserSchema().load(request.get_json())  # noqa : F841
        user_request = UserRequest(user_schema=user_schema)
        result = None
        with db.session.begin():
            user = User.query.filter_by(email=user_request.email).first()
            if user is not None:
                return "User already exists", 409
            result = user_request.get_user_model()
            db.session.add(result)
            return json.dumps(result.to_dict()), 200

    except ValidationError as ve:
        logging.error(ve.messages)
        return ve.messages, 403
