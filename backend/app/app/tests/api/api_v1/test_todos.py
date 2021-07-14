from datetime import date
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.todo import create_random_todo
from app.schemas.todo import PriorityEnum


def test_create_todo(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo Todo",
            "description": "Fus Do Rah!",
            "priority": PriorityEnum.LOW,
            "due_date": date.today(),
            }
    response = client.post(
        f"{settings.API_V1_STR}/todos/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content
    assert content['due_date'] == data['due_date']
    assert content['priority'] == data['priority']
    assert content['is_completed'] is False


def test_read_todo(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    item = create_random_todo(db)
    response = client.get(
        f"{settings.API_V1_STR}/todos/{item.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == item.id
    assert content["owner_id"] == item.owner_id
    assert content['due_date'] == item.due_date
    assert content['priority'] == item.priority
    assert content['is_completed'] == item.is_completed
