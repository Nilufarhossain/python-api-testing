
from helpers.api_client import create_user


def test_create_user():
    new_user = {
        "name": "Nilufar",
        "username": "qa_tester",
        "email": "qa.tester@example.com"
    }

    response = create_user(new_user)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == new_user["name"]
    assert response_data["email"] == new_user["email"]
    assert "id" in response_data
