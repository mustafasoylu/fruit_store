from werkzeug.exceptions import HTTPException
from src.common.constants import BUCKET_LIMIT


class JsonToDtoParsingError(HTTPException):
    code = 400
    description = "Request has missing fields"
    name = "Bad Request"


class RowToJsonParsingError(HTTPException):
    code = 500
    description = "Failed reading database row"
    name = "Internal Error"


class InvalidFruitError(HTTPException):
    def __init__(self, fruit_name: str):
        self.fruit_name = fruit_name

    @property
    def code(self):
        return 400

    @property
    def description(self):
        return f"Fruit '{self.fruit_name}' is not valid"


class InvalidFruitCountTypeError(HTTPException):
    @property
    def code(self):
        return 400

    @property
    def description(self):
        return f"Fruit type is not valid, must be int"


class EmptyBucketError(HTTPException):
    @property
    def code(self):
        return 400

    @property
    def description(self):
        return f"At least one fruit must be updated"


class InvalidFruitCountError(HTTPException):
    def __init__(self, fruit_name: str, fruit_count: int):
        self.fruit_name = fruit_name
        self.fruit_count = fruit_count

    @property
    def code(self):
        return 400

    @property
    def description(self):
        return f"Fruit count for '{self.fruit_name}' have to between 0 and {BUCKET_LIMIT} but was {self.fruit_count}"
