from app import app
from flask import redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app.secret_key = "!secret"
app.config.from_object("config")

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth = OAuth(app)
oauth.register(
    name="google",
    server_metadata_url=CONF_URL,
    client_kwargs={"scope": "openid email profile"},
)


@app.route("/")
def homepage():
    user = session.get("user")
    return "Hello World"


@app.route("/login")
def login():
    redirect_uri = url_for("auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route("/auth")
def auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    email = user["email"]
    print(email)
    session["user"] = user
    return redirect("/")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    app.run()
