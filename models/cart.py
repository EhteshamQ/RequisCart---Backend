from sqlalchemy import Column, ForeignKey
from app import db
from uuid import uuid4
from .cart_item_mapper import cart_item_mapper
from models.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Cart(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    cart_item_mapper = db.relationship(
        "Item",
        secondary=cart_item_mapper,
        lazy="subquery",
        backref=db.backref("cart", lazy=True),
    )

    def __str__(self):
        return f"<Cart : {self.id} ,  user_id : {self.user_id} >"

    def __repr__(self):
        return f"<Cart : {self.id} ,  user_id : {self.user_id} >"
