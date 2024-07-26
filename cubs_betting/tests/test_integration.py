import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def get_token():
    response = client.post("/token", data={"username": "user1", "password": "password1"})
    return response.json()["access_token"]

def test_get_odds_integration(get_token):
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/odds/1", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_betting_scores_integration(get_token):
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/betting-scores/1", headers=headers)
    assert response.status_code == 200
    assert "score" in response.json()

def test_get_historical_data_integration(get_token):
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/v1/historical-data", json={"start_date": "2022-01-01", "end_date": "2022-01-31"}, headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_custom_analysis_integration(get_token):
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/v1/custom-analysis", json={"data": {}}, headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
