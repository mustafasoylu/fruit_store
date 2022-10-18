from src.common.constants import DEBUG
import logging
from logging.handlers import TimedRotatingFileHandler
from os import path, makedirs


def _create_dir_if_not_exists(name: str) -> None:
    if not path.exists(name):
        makedirs(name)


def _get_handler() -> None:
    folder = "logs"
    file_name = "app.log"
    _create_dir_if_not_exists(folder)
    logger_name = f"{folder}/{file_name}"

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    handler = TimedRotatingFileHandler(logger_name, when="midnight", backupCount=30)

    handler.setFormatter(formatter)
    return handler


def set_basic_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG if DEBUG else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        handlers=[_get_handler()],
    )


def log_request(name: str, request):
    method = request.method
    route = request.path

    logger = get_logger(name)
    logger.info(f"Processing {method} {route}")


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    return logger
