import pytest
from clients.users.public_users_client import get_public_users_client, PublicUsersClient


@pytest.fixture(scope="function")
def public_users_client()-> PublicUsersClient:
    return get_public_users_client()
