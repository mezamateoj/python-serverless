from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_resource():
    response = client.get(f"/")
    assert response.status_code == 200


def test_child_resource():
    response = client.get(f"/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hi There from api/v1. try /api/v1/url/ and pass a job url as a json body"}