import pytest
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.assertions.schema import validate_json_schema
import allure

@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.feature(AllureFeatures.USERS)
class TestUsers:

    @allure.title("Create User")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStories.CREATE_ENTITY)
    def test_create_user(self, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # assert response.status_code == HTTPStatus.OK, "Некорректный статус-код ответа"
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Get User me")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStories.GET_ENTITY)
    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user: UserFixture):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate(response.json())

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
