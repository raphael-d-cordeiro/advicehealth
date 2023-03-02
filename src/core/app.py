import os

from flask import Flask, abort

from dotenv import load_dotenv

from src.main.routes.v1 import (
    car_owner_routes_bp, car_routes_bp, sales_routes_bp
)

from src.core.models import create_database
from src.core.database import DBConnection

load_dotenv()
create_database(DBConnection().get_engine())


app = Flask(__name__)


app.register_blueprint(car_owner_routes_bp)
app.register_blueprint(car_routes_bp)
app.register_blueprint(sales_routes_bp)


@app.route("/hello-world")
def hello_work():
    """Hello World route"""
    return "Hello World! The API is Running!"
