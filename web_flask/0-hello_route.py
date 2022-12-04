#!/usr/bin/python3
"""
file: 0-hello_route.py
desc: This module runs a simple flask app.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Nov 10, 2022
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB! from the root path"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
