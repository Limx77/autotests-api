from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateUserRequest(TypedDict):
    """
    Класс для аннотации передаваемого словаря в request create_user_api
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequest)-> Response:
        """
        Метод для создания нового юзера api/v1/users
        :param request: словарь CreateUserRequest
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url= "api/v1/users",json=request)