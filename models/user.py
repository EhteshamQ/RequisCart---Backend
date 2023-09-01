from enum import Enum
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import LargeBinary, String
from sqlalchemy.dialects.postgresql import UUID

from app import db
from models.base import Base


class Role(Enum):
    ADMIN = "ADMIN"
    USER = "USER"

    @staticmethod
    def get_matching_value(value: str):
        for member in Role:
            if member.value == value:
                return member
        raise ValueError(f"No Matching Value for {value}")


class Status(Enum):
    ACTIVE = "ACTIVE"
    INVITED = "INVITED"
    DELETED = "DELETED"

    @staticmethod
    def get_matching_value(value: str):
        for member in Status:
            if member.value == value:
                return member
        raise ValueError(f"No Matching Value for {value}")


class User(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String, nullable=False, unique=True)
    date_of_birth = Column(DateTime, nullable=True)
    status = Column(SqlEnum(Status), nullable=False)
    role = Column(SqlEnum(Role), nullable=False)
    picture = Column(LargeBinary, nullable=True)
    cart = db.relationship("Cart", backref="user", lazy=True)
    payment = db.relationship("Payment", backref="user", lazy=True)
    order = db.relationship("Order", backref="user", lazy=True)
    password = Column(
        String,
        nullable=False,
    )
    is_deleted = Column(Boolean, nullable=False, default=False)

    def __str__(self):
        return f"<User : {self.id} ,  name : {self.name} >"

    def __repr__(self):
        return f"<User : {self.id} ,  name : {self.name} >"

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "picture": self.picture,
            "role": self.role.name,
            "status": self.status.name,
            "date_of_birth": str(self.date_of_birth),
            "name": self.name,
        }

    # to do write a method to get user response
    def get_user_response():
        pass
