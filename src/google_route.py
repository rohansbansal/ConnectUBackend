from flask import Blueprint

google_auth = Blueprint("google_auth", __name__)


@google_auth.route("/login/google/authorized", methods=["GET"])
def test():
    return "it works!"
