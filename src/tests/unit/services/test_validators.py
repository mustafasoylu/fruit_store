import unittest
from src.services.validators import (
    validate_fruit_count,
    validate_fruit_type,
    validate_dict_key,
    validate_fruits_instance,
    validate_count_instance,
    validate_dict_length,
)
from src.services.exceptions import (
    JsonToDtoParsingError,
    InvalidFruitError,
    InvalidFruitCountTypeError,
    EmptyBucketError,
    InvalidFruitCountError,
)


class TestValidators(unittest.TestCase):
    VALID_COUNT = 10
    INVALID_COUNT = 1001
    INVALID_COUNT2 = -1

    VALID_FRUIT = "apple"
    INVALID_FRUIT = "kiwi"

    VALID_DICT = {"fruits": {"apple": 10}}
    INVALID_DICT = {"test": {"apple": 10}}

    INVALID_FRUITS_INSTANCE = ["apple", "banana"]

    INVALID_COUNT_INSTANCE = "10"
    INVALID_DICT_LENGTH = {}

    def test_validate_fruit_count(self):
        # valid count
        try:
            validate_fruit_count(self.VALID_FRUIT, self.VALID_COUNT)
        except InvalidFruitCountError:
            self.fail("validate_fruit_count raised Exception unexpectedly!")

    def test_validate_fruit_count_invalid(self):
        # invalid count
        with self.assertRaises(InvalidFruitCountError):
            validate_fruit_count(self.VALID_FRUIT, self.INVALID_COUNT)

        with self.assertRaises(InvalidFruitCountError):
            validate_fruit_count(self.VALID_FRUIT, self.INVALID_COUNT2)

    def test_validate_fruit_type(self):
        # valid fruit
        try:
            validate_fruit_type(self.VALID_FRUIT)
        except InvalidFruitError:
            self.fail("validate_fruit_type raised Exception unexpectedly!")

    def test_validate_fruit_type_invalid(self):
        # invalid fruit
        with self.assertRaises(InvalidFruitError):
            validate_fruit_type(self.INVALID_FRUIT)

    def test_validate_dict_key(self):
        # valid dict
        try:
            validate_dict_key(self.VALID_DICT)
        except JsonToDtoParsingError:
            self.fail("validate_dict_key raised Exception unexpectedly!")

    def test_validate_dict_key_invalid(self):
        # invalid dict
        with self.assertRaises(JsonToDtoParsingError):
            validate_dict_key(self.INVALID_DICT)

    def test_validate_fruits_instance(self):
        try:
            validate_fruits_instance(self.VALID_DICT["fruits"])
        except JsonToDtoParsingError:
            self.fail("validate_fruits_instance raised Exception unexpectedly!")

    def test_validate_fruits_instance_invalid(self):
        with self.assertRaises(JsonToDtoParsingError):
            validate_fruits_instance(self.INVALID_FRUITS_INSTANCE)

    def test_validate_count_instance(self):
        try:
            validate_count_instance(self.VALID_COUNT)
        except InvalidFruitCountTypeError:
            self.fail("validate_count_instance raised Exception unexpectedly!")

    def test_validate_count_instance_invalid(self):
        with self.assertRaises(InvalidFruitCountTypeError):
            validate_count_instance(self.INVALID_COUNT_INSTANCE)

    def test_validate_dict_length(self):
        try:
            validate_dict_length(self.VALID_DICT["fruits"])
        except EmptyBucketError:
            self.fail("validate_dict_length raised Exception unexpectedly!")

    def test_validate_dict_length_invalid(self):
        with self.assertRaises(EmptyBucketError):
            validate_dict_length(self.INVALID_DICT_LENGTH)
