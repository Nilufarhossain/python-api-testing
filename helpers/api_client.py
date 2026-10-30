
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    return requests.get(
        f"{BASE_URL}/users",
        timeout=10
    )


def get_user(user_id):
    return requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )


def create_user(data):
    return requests.post(
        f"{BASE_URL}/users",
        json=data,
        timeout=10
    )


def update_user(user_id, data):
    return requests.put(
        f"{BASE_URL}/users/{user_id}",
        json=data,
        timeout=10
    )


def delete_user(user_id):
    return requests.delete(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )
