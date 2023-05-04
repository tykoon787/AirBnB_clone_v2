#!/usr/bin/python3
"""
This module starts a flask app on port 0.0.0.0

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Function to Return '/' route"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
