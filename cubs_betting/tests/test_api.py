import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Cubs Betting Analytics API"}

def test_get_odds_unauthorized():
    response = client.get("/api/v1/odds/1")
    assert response.status_code == 401

def test_get_betting_scores_unauthorized():
    response = client.get("/api/v1/betting-scores/1")
    assert response.status_code == 401

def test_get_historical_data_unauthorized():
    response = client.post("/api/v1/historical-data", json={"start_date": "2022-01-01", "end_date": "2022-01-31"})
    assert response.status_code == 401

def test_custom_analysis_unauthorized():
    response = client.post("/api/v1/custom-analysis", json={"data": {}})
    assert response.status_code == 401

def test_login():
    response = client.post("/token", data={"username": "user1", "password": "password1"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_odds_authorized():
    login_response = client.post("/token", data={"username": "user1", "password": "password1"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/odds/1", headers=headers)
    assert response.status_code == 200

def test_get_betting_scores_authorized():
    login_response = client.post("/token", data={"username": "user1", "password": "password1"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/betting-scores/1", headers=headers)
    assert response.status_code == 200

def test_get_historical_data_authorized():
    login_response = client.post("/token", data={"username": "user1", "password": "password1"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/v1/historical-data", json={"start_date": "2022-01-01", "end_date": "2022-01-31"}, headers=headers)
    assert response.status_code == 200

def test_custom_analysis_authorized():
    login_response = client.post("/token", data={"username": "user1", "password": "password1"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/v1/custom-analysis", json={"data": {}}, headers=headers)
    assert response.status_code == 200
