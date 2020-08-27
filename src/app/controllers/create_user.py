from flask import Blueprint

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/user/api", methods=["GET"])
def getUser():
    return "user"
