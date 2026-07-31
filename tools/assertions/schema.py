from typing import Any

import allure
from jsonschema import validate, FormatChecker

@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    validate(instance=instance, schema=schema, format_checker=FormatChecker())

def validate_json_schema_get_user(instance: Any, schema: dict) -> None:
    validate(instance=instance, schema=schema, format_checker=FormatChecker())