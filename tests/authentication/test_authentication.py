import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
import allure

@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.feature(AllureFeatures.AUTHENTICATION)
class TestAuthentication:
    @allure.title("Logit with correct email and password")
    @allure.story(AllureStories.LOGIN)
    def test_login_user(self, authentication_client: AuthenticationClient, function_user: UserFixture):
        request = LoginRequestSchema(email= function_user.email, password= function_user.password)
        login_response = authentication_client.login_api(request)
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

        assert_status_code(login_response.status_code, HTTPStatus.OK)
        assert_login_response(login_response_data)

        validate_json_schema(login_response.json(), login_response_data.model_json_schema())