#!/usr/bin/python3
"""
Starts a flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """
    handles '/' route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    handles '/hbnb' route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    handles '/c/<text>' route and returns
    'c text..'
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
