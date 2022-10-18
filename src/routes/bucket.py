from flask import request
from src.routes.dto.bucket import PostRequest
from src.routes.dto.common import SuccessResponse
from .utils.validators import validate_content_type
from src.services.bucket import get_bucket_service
from . import routes
from .utils.handlers import router_handler
from src.routes.utils.parsers import PostRequestMapper, GetResponseMapper
from src.utils.log import get_logger
from src.utils.log import log_request


logger = get_logger(__name__)


@routes.route("/bucket", methods=["GET", "POST"])
@router_handler
def buckets():
    bucket_service = get_bucket_service()
    log_request(__name__, request)
    if request.method == "GET":
        row = bucket_service.find()
        response = GetResponseMapper.from_row(row)
        return response
    elif request.method == "POST":
        content_type = request.headers.get("Content-Type")
        validate_content_type(content_type)

        add_request: PostRequest = PostRequestMapper.from_json(request.get_json())
        bucket_service.add_row(add_request)
        return SuccessResponse(message="Added row")


@routes.route("/bucket/<float:timestamp>")
@routes.route("/bucket/<int:timestamp>")
@router_handler
def bucket_find(timestamp):
    bucket_service = get_bucket_service()
    log_request(__name__, request)
    row = bucket_service.find(timestamp)

    response = GetResponseMapper.from_row(row)
    return response
