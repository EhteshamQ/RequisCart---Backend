from datetime import datetime
from typing import Optional
from uuid import UUID

from attr import dataclass
from models.user import Role, Status, User as UserModel


@dataclass(frozen=True)
class UserResponse:
    id: str
    name: str
    email: str
    date_of_birth: Optional[datetime]
    role: Role
    status: Status
    picture: Optional[bytes]

    def __init__(self, user_model: UserModel):
        self.id = UUID(user_model.id).hex
        self.date_of_birth = user_model.date_of_birth
        self.email = user_model.email
        self.role = user_model.role
        self.status = user_model.status
        self.picture = user_model.picture
        self.name = user_model.name

    def __str__(self):
        return f"<User Response with {self.id} and name {self.name}>"
