#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """
    fetches states and their cities from DB and
    renders them asc order
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(exc):
    """
    closes session after every request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
