#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    fetches states list from DB and renders them asc order
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exc):
    """
    closes session after every request
    """
    storage.close()


if __name__ == "__main__":
    app.run()
