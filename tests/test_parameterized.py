
import pytest
from helpers.api_client import get_user


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_multiple_users(user_id):
    response = get_user(user_id)

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == user_id
    assert "name" in user
    assert "email" in user
