from datetime import datetime
import json
from models.user import Role, Status, User
from bcrypt import hashpw, gensalt


class UserRequest:
    name: str
    password: str
    date_of_birth: datetime
    picture: bytes
    status: Status
    role: Role
    email: str

    def __init__(self, user_schema: dict):
        for key, value in user_schema.items():
            setattr(self, key, value)
        self.password = str(
            hashpw(
                password=bytes(self.password, "utf8"),
                salt=gensalt(),
            ),
            "utf8",
        )

    def get_user_model(self):
        user = User()
        user.name = self.name
        user.email = self.email
        user.date_of_birth = self.date_of_birth
        user.status = self.status
        user.role = self.role
        user.password = self.password
        return user

    def __str__(self):
        print(vars(self))
        return json.dumps(vars(self), default=str)
