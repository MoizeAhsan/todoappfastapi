from datetime import timezone
import datetime
import enum
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Enum

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class PriorityEnum(enum.Enum):
    """Priority class enums.

    Args:
        Enum ([type]): [description]
    """
    NONE = 'None'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class Todo(Base):

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    due_date = Column(Date, default=datetime.datetime.utcnow().date)
    priority = Column(Enum(PriorityEnum,
                           values_callable=lambda obj: [e.value for e in obj]),
                      default=PriorityEnum.NONE.value,
                      server_default=PriorityEnum.NONE.value,
                      nullable=False,
                      )
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="todos")
