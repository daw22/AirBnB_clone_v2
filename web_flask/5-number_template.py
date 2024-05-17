#!/usr/bin/python3
"""
Starts a flask web application
"""
from flask import Flask, render_template


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text=None):
    """
    handles '/python/text route, returns
    'Python text...'
    """
    if text is None:
        return "Python is cool"
    else:
        return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    handels '/number/n' route
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    handles '/number_templates/n' route
    renders a template with number=n as value
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run()
