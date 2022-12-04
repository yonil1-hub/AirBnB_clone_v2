#!/usr/bin/python3
"""
file: 10-hbnb_filters.html
Desc: This python module executes simple flask application over the AirBnB site
      written for the ALX higher level programming track.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Nov 13, 2022
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters_for_airbnb():
    """Displays some data from db on the AirBnB website."""
    states = storage.all("State")
    amenity = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", s=states, am=amenity)


@app.teardown_appcontext
def tear_down_db(execute):
    """Removes the current SQLAlchemy session after each request
    is completed"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
