import pytest

@pytest.fixture(scope="function")
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


@pytest.fixture(scope="function")
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")

"""
Такой декоратор позволяет применять указанные фикстуры во всех тестах класса,
не передавая явно эти фикстуры в каждый тест!
То есть все тесты буду использовать указанные фикстуры!
Как правило такое используется для фикстур, которые не возвращают конкретные значения. 
То есть если фикстура значений не возвращает, например очистка БД. Какое-то обобщенное действие.
"""
@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...