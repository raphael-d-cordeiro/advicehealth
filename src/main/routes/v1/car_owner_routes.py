from flask import Blueprint, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from src.main.composer import (
    add_car_owner_composer,
    list_car_owner_composer,
)
from src.main.adapter import flask_route_adapter


car_owner_routes_bp = Blueprint(
    "car_owner_routes", __name__, url_prefix="/v1/carowners"
)

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


@car_owner_routes_bp.route("/", methods=["POST"])
@auth.login_required
def register_car_owner():
    """register car owner route"""

    return flask_route_adapter(request=request, api_controller=add_car_owner_composer())


@car_owner_routes_bp.route("/", methods=["GET"])
@auth.login_required
def list_car_owners():
    """List car owners route"""

    return flask_route_adapter(
        request=request, api_controller=list_car_owner_composer()
    )
