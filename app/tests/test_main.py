from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main_resource():
    response = client.get(f"/")
    assert response.status_code == 200

def test_child_resource():
    response = client.get(f"/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": "Try /api/v1/url/ and pass a jo url"}