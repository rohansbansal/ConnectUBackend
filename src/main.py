import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


if __name__ == "__main__":
    app.run()
