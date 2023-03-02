from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request

from src.main.composer import (
    add_car_composer,
)
from src.main.adapter import flask_route_adapter

car_routes_bp = Blueprint("car_routes", __name__, url_prefix="/v1/cars")


auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@car_routes_bp.route("/", methods=["POST"])
@auth.login_required
def register_car():
    """register car route"""

    return flask_route_adapter(request=request, api_controller=add_car_composer())


@car_routes_bp.route("/", methods=["GET"])
def list_car():
    """list car route"""

    return
