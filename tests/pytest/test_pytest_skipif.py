import pytest

SYSTEM_VERSION = "V1.2.0"

@pytest.mark.skipif(SYSTEM_VERSION == "V1.1.0", reason="only V1.3.0 supported")
def test_system_version_valid():
    ...

@pytest.mark.skipif(SYSTEM_VERSION == "V1.2.0", reason="only V1.2.0 supported")
def test_system_version_invalid():
    ...
"""
Маркер skipif позволяет пропустить какой-то тест, если условие верно/истинно. Если false, то тест запускается.
Условие передается в качестве аргумента, при этом аргумент reason в skipif
является обязательным в отличие от просто skip
"""