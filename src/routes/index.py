from flask import render_template
from . import routes


@routes.route("/", methods=["GET"])
@routes.route("/index.html", methods=["GET"])
@routes.route("/index", methods=["GET"])
@routes.route("/home", methods=["GET"])
def index():
    return render_template("index.html")


@routes.route("/update.html", methods=["GET"])
@routes.route("/update", methods=["GET"])
def update():
    return render_template("update.html")
