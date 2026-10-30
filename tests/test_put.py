
from helpers.api_client import update_user


def test_update_user():
    updated_user = {
        "name": "Nilufar Updated",
        "username": "qa_tester",
        "email": "updated.qa@example.com"
    }

    response = update_user(1, updated_user)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["name"] == updated_user["name"]
    assert response_data["email"] == updated_user["email"]
    assert response_data["id"] == 1