from app import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

cart_item_mapper = db.Table(
    "cart_item_mapper",
    Column("cart_id", UUID(as_uuid=True), ForeignKey("cart.id"), primary_key=True),
    Column("item_id", UUID(as_uuid=True), ForeignKey("item.id"), nullable=False),
)
