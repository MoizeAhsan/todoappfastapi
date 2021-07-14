from sqlalchemy.orm import Session

from app import crud
from app.schemas.todo import TodoCreate, TodoUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    assert todo.title == title
    assert todo.description == description
    assert todo.owner_id == user.id


def test_get_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    stored_todo = crud.todo.get(db=db, id=todo.id)
    assert stored_todo
    assert todo.id == stored_todo.id
    assert todo.title == stored_todo.title
    assert todo.description == stored_todo.description
    assert todo.owner_id == stored_todo.owner_id


def test_update_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    description2 = random_lower_string()
    todo_update = TodoUpdate(description=description2)
    todo2 = crud.todo.update(db=db, db_obj=todo, obj_in=todo_update)
    assert todo.id == todo2.id
    assert todo.title == todo2.title
    assert todo2.description == description2
    assert todo.owner_id == todo2.owner_id


def test_delete_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    user = create_random_user(db)
    todo = crud.todo.create_with_owner(db=db, obj_in=todo_in, owner_id=user.id)
    todo2 = crud.todo.remove(db=db, id=todo.id)
    todo3 = crud.todo.get(db=db, id=todo.id)
    assert todo3 is None
    assert todo2.id == todo.id
    assert todo2.title == title
    assert todo2.description == description
    assert todo2.owner_id == user.id
