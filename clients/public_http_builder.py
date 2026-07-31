import allure
from httpx import Client

@allure.step('get public http client')
def get_public_http_client():
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(timeout=100, base_url='http://localhost:8000')



