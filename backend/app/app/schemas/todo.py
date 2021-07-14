from datetime import date
from typing import Hashable, Optional, Union

import enum
from pydantic import BaseModel


# Shared properties

class PriorityEnum(str, enum.Enum):
    """Priority enum class.

    Args:
        str ([type]): [description]
        enum ([type]): [description]
        Enum ([type]): [description]
    """
    NONE = 'NONE'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'


class TodoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Union[bool,None] = False
    due_date: Optional[date] = None
    priority: Optional[PriorityEnum] = PriorityEnum.NONE

    # Properties to receive on item creation


class TodoCreate(TodoBase):
    title: str


# Properties to receive on item update
class TodoUpdate(TodoBase):
    pass


# Properties shared by models stored in DB
class TodoInDBBase(TodoBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Todo(TodoInDBBase):
    pass


# Properties properties stored in DB
class TodoInDB(TodoInDBBase):
    pass
