from flask import Blueprint

routes = Blueprint("routes", __name__)


from .index import *
from .bucket import *
