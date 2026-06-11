import pytest


@pytest.mark.skip(reason="skip test")
def test_feature_in_development():
    ...
"""
Маркек skip позволяет просто пропустить тест,
например если фича еще не готова, а мы уже написали тест
также можно передать аргумент reason указав причину пропуска
"""
