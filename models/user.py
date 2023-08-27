from app import db
from enum import Enum
from uuid import uuid4
from sqlalchemy import Column, String, Enum as SqlEnum, LargeBinary, DateTime
from models.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Role(Enum):
    ADMIN = "admin"
    USER = "user"


class Status(Enum):
    ACTIVE = "active"
    INVITED = "invited"
    DELETED = "deleted"


class User(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String, nullable=False, unique=True)
    date_of_birth = Column(DateTime, nullable=True)
    status = Column(SqlEnum(Status), nullable=False)
    role = Column(SqlEnum(Role), nullable=False)
    picture = Column(LargeBinary, nullable=True)
    cart = db.relationship("Order", backref="user", lazy=True)
    payment = db.relationship("Payment", backref="user", lazy=True)
    order = db.relationship("Order", backref="user", lazy=True)
    password = Column(String, nullable=False)

    def __str__(self):
        return f"<User : {self.id} ,  name : {self.name} >"

    def __repr__(self):
        return f"<User : {self.id} ,  name : {self.name} >"
