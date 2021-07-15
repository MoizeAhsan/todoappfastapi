from datetime import timezone
import datetime
import enum
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, undefer
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Enum
from sqlalchemy_utils.types.choice import ChoiceType

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Todo(Base):
    TYPES = [
        (u'NONE', u'None'),
        (u'LOW', u'Low'),
        (u'MEDIUM', u'Medium'),
        (u'HIGH', u'High')
    ]
    TYPES_DICT = {
        u'NONE': u'None',
        u'LOW': u'Low',
        u'MEDIUM': u'Medium',
        u'HIGH': u'High'
    }
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=False, nullable=True)
    due_date = Column(Date, default=datetime.datetime.utcnow().date)
    priority = Column(ChoiceType(TYPES), nullable=False,
                      default='NONE', server_default='NONE')
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="todos")
