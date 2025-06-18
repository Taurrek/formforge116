import os
import pytest
from fastapi.testclient import TestClient
from backend_marketplace_api import app
from modules.db import Base, engine, SessionLocal
from modules.marketplace import DrillPack

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_upload_and_list(tmp_path, monkeypatch):
    # Create a dummy file to upload
    dummy = tmp_path / "dummy.zip"
    dummy.write_bytes(b"content")

    # Monkeypatch UPLOAD_DIR to tmp_path
    monkeypatch.setenv("UPLOAD_DIR", str(tmp_path))

    # Upload
    response = client.post(
        "/marketplace/upload",
        data={
            "coach_id": 1,
            "title": "Test Pack",
            "description": "Desc",
            "price_cents": 1000
        },
        files={"file": ("dummy.zip", dummy.read_bytes())}
    )
    assert response.status_code == 200
    pack = response.json()["drill_pack"]
    assert "id" in pack and "file_url" in pack

    # List
    resp2 = client.get("/marketplace/list")
    assert resp2.status_code == 200
    items = resp2.json()
    assert any(i["id"] == pack["id"] for i in items)
