from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import datetime

from db.base_class import Base


class Post(Base):
    uid = Column(UUIDType, default=uuid4, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(UUIDType, ForeignKey("user.uid"))
    owner = relationship("User", back_populates="post")
