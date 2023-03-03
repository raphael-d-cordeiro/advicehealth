import os

from flask import Flask, abort
from flask_cors import CORS

from dotenv import load_dotenv

from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python import get_all_cors_headers
from supertokens_python.recipe import emailpassword, session
from supertokens_python.framework.flask import Middleware

from src.main.routes.v1 import (
    car_owner_routes_bp, car_routes_bp, sales_routes_bp
)

from src.core.models import create_database
from src.core.database import DBConnection

load_dotenv()
create_database(DBConnection().get_engine())


init(
    app_info=InputAppInfo(
        app_name="advicehealtrh",
        api_domain="http://localhost:3567",
        website_domain="http://localhost:8000",
        api_base_path="/auth",
        website_base_path="/auth",
    ),
    supertokens_config=SupertokensConfig(
        connection_uri=os.environ.get('SUPERTOKENS_CONNECTION_URI'),
        # api_key=os.environ.get('SUPERTOKENS_API_KEY')
    ),
    framework="flask",
    # initializes session features
    recipe_list=[
        session.init(
            jwt=session.JWTConfig(enable=True,
                                  issuer='https://0d53-2405-201-e-d8bd-587b-3674-124d-4208.ngrok.io/auth')
        ),
        emailpassword.init()
    ],
)

app = Flask(__name__)
Middleware(app)

CORS(
    app=app,
    origins=["http://localhost:8000"],
    supports_credentials=True,
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)

app.register_blueprint(car_owner_routes_bp)
app.register_blueprint(car_routes_bp)
app.register_blueprint(sales_routes_bp)


@app.route("/hello-world")
def hello_work():
    """Hello World route"""
    return "Hello World! The API is Running! and docker too"


# This is required since if this is not there, then OPTIONS requests for
# the APIs exposed by the supertokens' Middleware will return a 404
@app.route("/", defaults={"u_path": ""})
@app.route("/<path:u_path>")
def catch_all(u_path: str):
    abort(404)
