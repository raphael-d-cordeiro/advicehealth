import uuid

from sqlalchemy import (
    Column,
    String,
)

from src.core.models.base import Base


class UserModel(Base):
    """Model class of Sqlachemy"""

    __tablename__ = "users"

    id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    login = Column(String(40))
    passwd = Column(String(40))
