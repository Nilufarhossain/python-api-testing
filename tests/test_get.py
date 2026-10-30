
from helpers.api_client import get_users, get_user


def test_get_users():
    response = get_users()

    assert response.status_code == 200
    assert len(response.json()) == 10


def test_get_invalid_user():
    response = get_user(99999)

    assert response.status_code == 404
    assert response.json() == {}
