import json
import logging
import time
from functools import wraps
from flask import Response


logger = logging.getLogger("Route Handler")


def router_handler(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            result = json.dumps(result)
        else:
            result = json.dumps(result.__dict__)
        logger.info(f"Response returned in {time.time() - start} seconds.")
        return Response(result, mimetype="application/json")

    return wrapped_func
