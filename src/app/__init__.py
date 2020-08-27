from os import environ
from app.utils.db_instance import mongo
from flask import Blueprint, Flask
from app.controllers.create_user import CreateUserController


# from app.controllers.create_preferences import GetUserController
# from app.controllers.get_user_info import *
# from app.controllers.get_preferences import *

user_bp = Blueprint("user_bp", __name__, url_prefix="/user/api")

user_controllers = [CreateUserController()]

for controller in user_controllers:
    user_bp.add_url_rule(
        controller.get_path(),
        controller.get_name(),
        controller.response,
        methods=controller.get_methods(),
    )

app = Flask(__name__)

app.config["MONGO_URI"] = environ["MONGO_URI"]
app.config["CLIENT_ID"] = environ["CLIENT_ID"]
app.config["CLIENT_SECRET"] = environ["CLIENT_SECRET"]


mongo.init_app(app)
app.register_blueprint(user_bp)
