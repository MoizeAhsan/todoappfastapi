from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.todo import create_random_todo


def test_create_todo(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo Todo", "description": "Fus Do Rah!"}
    response = client.post(
        f"{settings.API_V1_STR}/todos/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


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
