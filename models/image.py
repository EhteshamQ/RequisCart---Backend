from uuid import uuid4
from sqlalchemy import Column, LargeBinary, Boolean, ForeignKey
from models.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Image(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    data = Column(LargeBinary, nullable=False)
    is_deleted = Column(Boolean, default=False)
    item_id = Column(UUID(as_uuid=True), ForeignKey("item.id"), nullable=False)

    def __str__(self):
        return f"<Image : {self.id} >"

    def __repr__(self):
        return f"<Image : {self.id} >"
