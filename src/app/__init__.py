from flask import Blueprint, Flask
from app.controllers.create_user import *
from app.controllers.create_preferences import *
from app.controllers.get_user_info import *
from app.controllers.get_preferences import *
from os import environ

user_bp = Blueprint("user_bp", __name__, url_prefix="/user/api")
preferences_bp = Blueprint("preferences_bp", __name__, url_prefix="preferences/api")

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(preferences_bp)
