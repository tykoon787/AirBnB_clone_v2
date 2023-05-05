#!/usr/bin/python3
"""
Cretes a flask app
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>
    /number/<n>: Displays "n" if int
    /number_odd_or_even/<n>: Display if <n> is even or odd
"""

from flask import Flask, render_template
from markupsafe import escape

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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C %s" % escape(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python %s" % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return "%d is a number" % (n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    if (n % 2 == 0):
        result = "is even"
    else:
        result = "is odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
