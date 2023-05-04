#!/usr/bin/python3
"""
Cretes a flask app with 2 routes
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns index
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns HBNB
    """
    return ("HBNB")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
