import unittest
from src.routes.utils.parsers import PostRequestMapper, GetResponseMapper
from src.services.exceptions import (
    JsonToDtoParsingError,
    InvalidFruitError,
    InvalidFruitCountTypeError,
    EmptyBucketError,
)
from src.services.exceptions import RowToJsonParsingError

from datetime import datetime


class TestPostRequestMapper(unittest.TestCase):
    VALID_RESPONSE = {"fruits": {"apple": -10, "banana": -20, "orange": 30}}

    INVALID_RESPONSE = {"test": {"apple": 10}}
    INVALID_RESPONSE2 = {"fruits": [{"apple": 10}]}
    INVALID_RESPONSE3 = {"fruits": {}}
    INVALID_RESPONSE4 = {"fruits": {"kiwi": 10}}
    INVALID_RESPONSE5 = {"fruits": {"apple": "10"}}

    def test_valid_response(self):
        try:
            PostRequestMapper.from_json(self.VALID_RESPONSE)
        except Exception:
            self.fail("from_json raised Exception unexpectedly!")

    def test_invalid_response(self):
        with self.assertRaises(JsonToDtoParsingError):
            PostRequestMapper.from_json(self.INVALID_RESPONSE)

    def test_invalid_response2(self):
        with self.assertRaises(JsonToDtoParsingError):
            PostRequestMapper.from_json(self.INVALID_RESPONSE2)

    def test_invalid_response3(self):
        with self.assertRaises(EmptyBucketError):
            PostRequestMapper.from_json(self.INVALID_RESPONSE3)

    def test_invalid_response4(self):
        with self.assertRaises(InvalidFruitError):
            PostRequestMapper.from_json(self.INVALID_RESPONSE4)

    def test_invalid_response5(self):
        with self.assertRaises(InvalidFruitCountTypeError):
            PostRequestMapper.from_json(self.INVALID_RESPONSE5)


class TestGetResponseMapper(unittest.TestCase):
    VALID_RESPONSE = {
        "fruits": {"apple": 10, "banana": 20, "orange": 30},
        "timestamp": datetime.now(),
    }
    INVALID_RESPONSE = {"test": "test"}

    def test_valid_response(self):
        try:
            GetResponseMapper.from_row(self.VALID_RESPONSE)
        except Exception:
            self.fail("from_row raised Exception unexpectedly!")

    def test_invalid_response(self):
        with self.assertRaises(RowToJsonParsingError):
            GetResponseMapper.from_row(self.INVALID_RESPONSE)
