import random
import pytest

PLATFORM = "Windows"

"""
reruns=3 — количество перезапусков. Если тест упадёт, он будет перезапущен до 3 раз.
reruns_delay=2 — задержка между перезапусками в секундах.
"""
@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуски реализуются на уровне маркировки flaky
def test_reruns():
    assert random.choice([True, False])

"""
Маркировка @pytest.mark.flaky также может быть использована для тестовых классов. 
Например, добавим тестовый класс TestReruns в файл test_reruns.py:
В таком случае реран будет работать для каждого теста из класса
"""
@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])

"""
В @pytest.mark.flaky можно задать условия для перезапуска, аналогично маркировке @pytest.mark.skipif. 
Добавим тест test_rerun_with_condition в файл test_reruns.py:
"""
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")  # Перезапуск при выполнении условия
def test_rerun_with_condition():
    assert random.choice([True, False])