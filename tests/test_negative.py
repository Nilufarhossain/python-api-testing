
from helpers.api_client import get_user, BASE_URL
import requests


# TC006: Verify invalid user ID returns 404
def test_invalid_user_id():
    response = get_user(999999)

    assert response.status_code == 404
    assert response.json() == {}


# TC007: Verify invalid API endpoint returns 404
def test_invalid_endpoint():
    response = requests.get(
        f"{BASE_URL}/invalid-endpoint",
        timeout=10
    )

    assert response.status_code == 404


# TC008: Verify user response contains required fields
def test_user_response_fields():
    response = get_user(1)

    assert response.status_code == 200

    user = response.json()

    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "username" in user
