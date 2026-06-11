import pytest


#Для запуска pytest с использованием меток используется ключ -m
@pytest.mark.smoke
def test_smoke_case():
    assert 1+1 == 2

@pytest.mark.regression
def test_regression_case():
    assert 2*2 == 4

@pytest.mark.fast
def test_fast():
    ...

@pytest.mark.slow
def test_slow():
    ...

@pytest.mark.smoke #Маркирова автоматически применяется ко всем тестам из класса
class TestSuite:
    def test_case1(self):
        ...
    def test_case2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    """
    В таком случае к тестам применяются две маркировки:
    маркировка класса и своя собственная
    """
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        ...

    def test_logout(self):
        ...