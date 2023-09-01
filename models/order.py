import datetime
from sqlalchemy import (
    ForeignKey,
    Column,
    DateTime,
    Float,
    Enum as SqlEnum,
)
from app import db
from uuid import uuid4
from enum import Enum
from models.base import Base
from models.order_item_mapper import order_item_mapper
from sqlalchemy.dialects.postgresql import UUID  # Rename these fields


class Status(Enum):
    DELIVERED = "DELIVERED"
    IN_TRANSIT = "IN_TRANSIT"
    PLACED = "PLACED"
    PROCESSING = "PROCESSING"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    CANCELLED = "CANCELLED"

    @staticmethod
    def get_matching_value(value: str):
        for member in Status:
            if member.value == value:
                return member
        raise ValueError(f"No Matching Value for {value}")


class Order(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    status = Column(SqlEnum(Status), nullable=False, default=Status.PROCESSING)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now())
    payment = db.relationship("Payment", backref="order", lazy=True)
    order_item_mapper = db.relationship(
        "Item",
        secondary=order_item_mapper,
        lazy="subquery",
        backref=db.backref("order", lazy=True),
    )

    def __str__(self):
        return f"<Order : {self.id} ,  user_id : {self.user_id} >"

    def __repr__(self):
        return f"<Order : {self.id} ,  user_id : {self.user_id} >"
