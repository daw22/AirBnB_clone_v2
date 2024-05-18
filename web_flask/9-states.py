#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """
    fetches states list from DB and renders them asc order
    """
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """
    fetches state and it's cities by id and
    renders the asc order
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def close_session(exc):
    """
    closes session after every request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
