from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
import pytest

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from pydantic import BaseModel, EmailStr


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self)->EmailStr:
        return self.request.email

    @property
    def password(self):
        return self.request.password

    @property
    def authentication_user(self):
        return AuthenticationUserSchema(email=self.email, password=self.password)

@pytest.fixture(scope="function")
def public_users_client()-> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture(scope="function")
def function_user(public_users_client: PublicUsersClient)-> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
