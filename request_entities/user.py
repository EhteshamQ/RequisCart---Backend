from datetime import datetime
from typing import Optional

from attr import dataclass

from models.user import Role, Status


@dataclass(frozen=True)
class UserRequest:
    name: str
    email: str
    date_of_birth: Optional[datetime]
    status: Status
    role: Role
    picture: Optional[bytes]
    password: str

    def __init__(self, user_request: dict):
        self.name = user_request["name"]
        self.email = user_request["email"]
        self.date_of_birth = (
            datetime.strptime(user_request["date_of_birth"], "%Y-%m-%d %H:%M:%S")
            if user_request["date_of_birth"] is not None
            else None
        )
        self.role = Role.get_matching_value(user_request.get("role"))
        self.status = Status.INVITED
        # TODO: Hash this before pushing to db
        self.password = user_request.get("password")
