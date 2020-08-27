from flask import Flask
from app.controllers.create_user import user_bp
from google_route import google_auth

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(google_auth)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
