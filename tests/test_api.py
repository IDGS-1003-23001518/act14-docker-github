from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_api_message_and_version():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "API publicada desde GitHub Container Registry",
        "version": "1.0.0",
    }


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}