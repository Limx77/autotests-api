import pytest
from _pytest.fixtures import SubRequest
"""
Реализация самой простой параметризации. Тут один аргумент number, который принимает значения из списка (второго аргумента)
"""
@pytest.mark.parametrize("number",[1,2,3,-1])
def test_numbers(number: int):
    assert number > 0

"""
Тут два аргумента, кототрые получают значения из распакованных таплов из списка(второго аргумента)
ВАЖНО передаваемые атрибуты писать через запятую в одних кавычках, чтобы это считался как один аргумент
иначе тест может выдать оишбку, так как 1ый аргумент это именование переменной, второй это сами переменные и третий какой-то другой параметр еще
"""
@pytest.mark.parametrize("number,expected",[(1,1), (2,4), (3,9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


"""
Тут происходит перемножение,то есть можно использовать 2-3 параметризации и они будут выполняться между собой 
то есть атрибут os будет выполнен для каждого атрибута host
"""
@pytest.mark.parametrize("os",["macos","windows", "debian", "linux"])
@pytest.mark.parametrize("host",[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


"""
Иногда нужно передать не только значения, но и дополнительную информацию, например, отметить, что тест должен быть пропущен или ожидать конкретного исключения. \
@pytest.mark.parametrize("value", [
    pytest.param(1),
    pytest.param(2),
    pytest.param(-1, marks=pytest.mark.skip(reason="Negative value")),
])
def test_increment(value):
    assert increment(value) > 0
    
В этом примере третий тест будет пропущен, так как он помечен pytest.mark.skip. 
Функция pytest.param() используется внутри декоратора @pytest.mark.parametrize для более тонкой настройки отдельных тестовых наборов. 
Она позволяет применить к конкретному набору данных специфические маркеры (например, skip или xfail) и задать уникальное имя (id) для удобства чтения отчетов.
"""

"""
Параметризовать можно не только тестовые функции, но и фикстуры. Это полезно, когда нужно передать разные параметры в фикстуру,
а затем использовать их в разных тестах.

@pytest.fixture(params=[value1, value2, value3])
def fixture_name(request):
    return request.param

def test_example(fixture_name):
    assert <some condition>
    
Пример:
import pytest

@pytest.fixture(params=[1000, 2000, 3000])
def port(request):
    return request.param

def test_port(port):
    assert port in [1000, 2000, 3000]
    
Здесь фикстура port будет передавать различные значения портов, 
и тест test_port выполнится три раза — по одному на каждый порт.
    
"""

'''
Иногда удобнее передавать значения в виде словарей, особенно если параметры могут изменяться:
@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
])
def test_login(data):
    assert login(data["username"], data["password"]) == "Success"
'''


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest)-> str:
    return request.param

#Если используемая фикстура параметризована, то тест параметризовать не нужно
def test_host(host:str):
    print(f"Rnning test on host: {host}")

"""
Можно прописать параметризацию к классу и она будет использована для
всех тестов в классе
"""
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations:{user}")



"""
аргумент ids помогает описать передаваемые значения, чтобы было понятно
что они означают. 
Кол-во идентификаторов(ids) должно быть равно кол-ву передаваемых значений
"""
@pytest.mark.parametrize(
    "phone_number",
    ["+7000011","+7000022", "+7000033"],
    ids=[
    "User with money",
    "User without money",
    "User with operations"
    ]
)
def test_identifiers(phone_number: str):
    pass

"""
Тут пример как в логах теста подставить значения
чтобы было видно и номер и его значениу
"""
users = {
    "+7000011": "User with money",
    "+7000022": "User without money",
    "+7000033": "User with operations"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}",
)
def test_identifiers_2(phone_number: str):
    pass