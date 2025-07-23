import pytest
from app import create_app
import os

@pytest.fixture
def client(tmp_path, monkeypatch):
    # point to isolated DB
    db_file = tmp_path / "test.db"
    monkeypatch.setenv("DATABASE_PATH", str(db_file))
    import init_db           # seeds test.db
    app = create_app()
    return app.test_client()

def test_get_all_users(client):
    rv = client.get("/users")
    assert rv.status_code == 200
    assert isinstance(rv.get_json(), list)

def test_get_not_found(client):
    rv = client.get("/user/9999")
    assert rv.status_code == 404

def test_create_and_login(client):
    payload = {"name":"X","email":"x@test.com","password":"abcdef"}
    rv = client.post("/users", json=payload)
    assert rv.status_code == 201
    new_user = rv.get_json()
    assert new_user["email"] == "x@test.com"

    rv2 = client.post("/login", json={"email":"x@test.com","password":"abcdef"})
    assert rv2.status_code == 200
    assert rv2.get_json()["status"] == "success"
