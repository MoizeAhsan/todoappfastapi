import random
from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.todo import PriorityEnum, TodoCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_bool, random_date, random_lower_string


def create_random_todo(db: Session, *, owner_id: Optional[int] = None) -> models.Todo:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    is_completed = random_bool()
    due_date = random_date()
    item_in = TodoCreate(title=title, description=description, id=id,
                         is_completed=is_completed, due_date=due_date,
                         priority=random.choice(list(PriorityEnum)))
    return crud.todo.create_with_owner(db=db, obj_in=item_in, owner_id=owner_id)
