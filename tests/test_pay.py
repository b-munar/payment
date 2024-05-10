import pytest
from unittest.mock import patch
from functools import wraps
import json

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : "9027aff6-545e-4a1c-bbf7-9c09f6ae595c"}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/payment/ping")
    assert response.status_code == 200
    assert b"pong" in response.data


def test_request_new_card(client):
    url = "/payment"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "card": "1234 5678 9012 6789",
        "date": "12/24",
        "cvv": "123",
        "name": "name sportman card"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201

def test_request_get_card(client):
    url = "/payment"
    headers = {
        "Content-Type": "application/json"
    }
    response = client.get(url, headers=headers)
    assert response.status_code == 200