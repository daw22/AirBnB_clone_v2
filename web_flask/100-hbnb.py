#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    fetches states, amenity and places list from DB
    and renders a page
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html", states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_session(exc):
    """
    closes session after every request
    """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
