from app.main import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "devops-demo-api"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_version():
    client = app.test_client()

    response = client.get("/api/version")

    assert response.status_code == 200

    data = response.get_json()

    assert data["version"] == "1.0.0"