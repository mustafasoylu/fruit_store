from flask import Flask
from flask_cors import CORS
from src.routes import *
from src.common.constants import API_HOST, API_PORT, DEBUG
from src.utils.log import get_logger, set_basic_logging


app = Flask("Fruit-Store", template_folder="src/templates")
app.register_blueprint(routes)
CORS(app)


def main():
    set_basic_logging()
    logger = get_logger(__name__)
    logger.info(f"Starting server on {API_HOST}:{API_PORT} and DEBUG={DEBUG}")
    app.run(host=API_HOST, port=API_PORT, debug=DEBUG)


def create_app():
    set_basic_logging()
    logger = get_logger(__name__)
    logger.info(f"Starting server on {API_HOST}:{API_PORT} and DEBUG={DEBUG}")
    return app


@app.after_request
def log_the_status_code(response):
    status = response.status_code
    method = request.method
    route = request.path

    logger = get_logger(__name__)
    logger.info(f"{method} {route} {status}")
    return response


if __name__ == "__main__":
    main()
