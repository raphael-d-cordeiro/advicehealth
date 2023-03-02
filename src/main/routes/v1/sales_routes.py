from flask import Blueprint, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from src.main.composer import (
    list_sale_opportunity_composer,
)
from src.main.adapter import flask_route_adapter

sales_routes_bp = Blueprint("sales_routes", __name__, url_prefix="/v1/sales")

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


@sales_routes_bp.route("/opportunity", methods=["GET"])
@auth.login_required
def list_sales_opportunity():
    """list sales opportunity route"""

    return flask_route_adapter(
        request=request, api_controller=list_sale_opportunity_composer()
    )
