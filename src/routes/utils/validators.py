from src.utils.log import get_logger

logger = get_logger(__name__)


def validate_content_type(content_type: str):
    if content_type != "application/json":
        logger.warning(f"Invalid content type: {content_type}")
        raise Exception("Only application/json is allowed")
