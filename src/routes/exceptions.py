from werkzeug.exceptions import HTTPException
from src.common.constants import BUCKET_LIMIT
from . import routes
from src.services.exceptions import (
    JsonToDtoParsingError,
    RowToJsonParsingError,
    InvalidFruitError,
    InvalidFruitCountTypeError,
    EmptyBucketError,
    InvalidFruitCountError,
)


@routes.errorhandler(HTTPException)
def handle_400(e):
    response_body = {
        "name": e.name,
        "description": e.description,
    }
    return response_body, e.code


@routes.errorhandler(HTTPException)
def handle_500(e):
    response_body = {
        "name": e.name,
        "description": e.description,
    }
    return response_body, e.code


routes.register_error_handler(InvalidFruitError, handle_400)
routes.register_error_handler(InvalidFruitCountError, handle_400)
routes.register_error_handler(InvalidFruitCountTypeError, handle_400)
routes.register_error_handler(EmptyBucketError, handle_400)
routes.register_error_handler(JsonToDtoParsingError, handle_400)
routes.register_error_handler(RowToJsonParsingError, handle_500)
