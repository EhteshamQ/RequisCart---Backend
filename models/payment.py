from uuid import uuid4
from enum import Enum

from models.base import Base
from sqlalchemy import Column
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Status(Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"


class Payment(Base):
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(SqlEnum(Status), nullable=False, default=Status.PENDING)
    order_id = Column(UUID(as_uuid=True), ForeignKey("order.id"), nullable=False)

    def __str__(self):
        return f"<Payment : {self.id} ,  user_id : {self.user_id.str()} , order_id : {self.order_id.str()} >"

    def __repr__(self):
        return f"<Payment : {self.id} ,  user_id : {self.user_id.str()} , order_id : {self.order_id.str()} >"
