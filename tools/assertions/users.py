from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, name="email")
    assert_equal(response.user.first_name, request.first_name, name="first_name")
    assert_equal(response.user.last_name, request.last_name, name="last_name")
    assert_equal(response.user.middle_name, request.middle_name, name="middle_name")

def assert_user(actual, expected):
    """
    Проверяет, что ответ на получение инфо пользователя соответствует запросу.

    :param actual: Исходный ответ на создание пользователя.
    :param expected: ожидаемый параметр
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.user.id, expected.user.id, name="id")
    assert_equal(actual.user.email, expected.user.email, name="email")
    assert_equal(actual.user.first_name, expected.user.first_name, name="first_name")
    assert_equal(actual.user.last_name, expected.user.last_name, name="last_name")
    assert_equal(actual.user.middle_name, expected.user.middle_name, name="middle_name")


def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на его создание.

    :param get_user_response: Ответ API при запросе данных пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    assert_user(get_user_response, create_user_response)