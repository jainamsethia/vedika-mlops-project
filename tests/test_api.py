from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_prediction():
    response = client.post(
        "/predict",
        json={"area": 1500, "bedrooms": 3, "bathrooms": 2, "age": 10, "distance_to_city": 10},
    )
    assert response.status_code == 200
    assert response.json()["predicted_price"] > 0


def test_invalid_area():
    response = client.post(
        "/predict",
        json={"area": 0, "bedrooms": 3, "bathrooms": 2, "age": 10, "distance_to_city": 10},
    )
    assert response.status_code == 422
