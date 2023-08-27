from app import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

order_item_mapper = db.Table(
    "order_item_mapper",
    Column("cart_id", UUID(as_uuid=True), ForeignKey("order.id"), primary_key=True),
    Column("item_id", UUID(as_uuid=True), ForeignKey("item.id"), primary_key=True),
)
