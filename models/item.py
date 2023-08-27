import datetime
from app import db
from uuid import uuid4
from sqlalchemy import Column, String, Boolean, Float, DateTime
from models.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Item(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)
    description = Column(String(200), nullable=False)
    date_added = Column(DateTime, nullable=False, default=datetime.datetime.now())
    images = db.relationship("Image", backref="item", lazy=True)

    def __str__(self):
        return f"<Item : {self.id} ,  name : {self.name} >"

    def __repr__(self):
        return f"<Item : {self.id} ,  name : {self.name} >"
