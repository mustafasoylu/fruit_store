from typing import Any
from src.common.constants import FRUITS, BUCKET_LIMIT
from src.services.exceptions import (
    JsonToDtoParsingError,
    InvalidFruitError,
    InvalidFruitCountTypeError,
    EmptyBucketError,
    InvalidFruitCountError,
)
from src.utils.log import get_logger

logger = get_logger(__name__)


def validate_fruit_count(fruit: str, count: int) -> bool:
    if not 0 <= count <= BUCKET_LIMIT:
        logger.debug(f"Invalid fruit count: {count}")
        raise InvalidFruitCountError(fruit, count)


def validate_fruit_type(fruit_name):
    if fruit_name not in FRUITS:
        logger.warning(f"Invalid fruit type: {fruit_name}")
        raise InvalidFruitError(fruit_name)


def validate_dict_key(dict: dict):
    if not "fruits" in dict:
        logger.warning(f"Invalid json: does not have fruits key")
        raise JsonToDtoParsingError()


def validate_fruits_instance(item: Any):
    if not isinstance(item, dict):
        logger.warning(f"Invalid json: fruits key is not an object type")
        raise JsonToDtoParsingError()


def validate_count_instance(item: Any):
    if not isinstance(item, int):
        logger.warning(f"Invalid json: fruit count is not an integer type")
        raise InvalidFruitCountTypeError()


def validate_dict_length(item: dict):
    if not len(item) > 0:
        logger.warning(f"Invalid json: object is empty")
        raise EmptyBucketError()
