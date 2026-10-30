
from helpers.api_client import delete_user


def test_delete_user():
    response = delete_user(1)

    assert response.status_code == 200
    assert response.json() == {}