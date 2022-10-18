from abc import ABC, abstractmethod
from typing import Dict
from src.routes.dto.bucket import PostRequest, GetResponse
from src.services.exceptions import RowToJsonParsingError
from src.services.validators import (
    validate_fruit_type,
    validate_dict_key,
    validate_fruits_instance,
    validate_dict_length,
    validate_count_instance,
)
from src.common.constants import FRUITS
from src.utils.log import get_logger

logger = get_logger(__name__)


class JsonToObjectMapper(ABC):
    @staticmethod
    @abstractmethod
    def from_json(json_data: Dict):
        pass


class PostRequestMapper(JsonToObjectMapper):
    @staticmethod
    def from_json(json_data: dict) -> PostRequest:
        validate_dict_key(json_data)
        validate_fruits_instance(json_data["fruits"])
        validate_dict_length(json_data["fruits"])

        fruits = {}
        for fruit in json_data["fruits"]:
            validate_fruit_type(fruit)
            fruit_count = json_data["fruits"][fruit]

            validate_count_instance(fruit_count)
            fruits[fruit] = int(fruit_count)

        return PostRequest(fruits=fruits)


class GetResponseMapper:
    @staticmethod
    def from_row(row: dict) -> GetResponse:
        try:
            timestamp = None
            fruits = dict.fromkeys(FRUITS, 0)
            if row:
                # convert datetime to unix timestamp
                timestamp = row["timestamp"].timestamp()

                # set counts
                for fruit in row["fruits"]:
                    fruits[fruit] = row["fruits"][fruit]

            return GetResponse(fruits=fruits, timestamp=timestamp)

        except KeyError as e:
            logger.warning(f"Invalid row: {e}")
            raise RowToJsonParsingError()
