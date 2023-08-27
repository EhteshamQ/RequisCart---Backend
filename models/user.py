from app import db
from enum import Enum
from uuid import uuid4
from sqlalchemy import Column, String, Enum as SqlEnum, LargeBinary, DateTime
from models.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Role(Enum):
    ADMIN = "admin"
    USER = "user"

    @staticmethod
    def get_matching_value(value: str):
        for member in Role:
            if member.value == value:
                return member
        raise ValueError(f"No Matching Value for {value}")


class Status(Enum):
    ACTIVE = "active"
    INVITED = "invited"
    DELETED = "deleted"

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
    password = Column(String, nullable=False)

    def __str__(self):
        return f"<User : {self.id} ,  name : {self.name} >"

    def __repr__(self):
        return f"<User : {self.id} ,  name : {self.name} >"
