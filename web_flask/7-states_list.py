#!/usr/bin/python3
"""
Returns a html with the list of states

Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>
    /number/<n>: Displays "n" if int
    /number_odd_or_even/<n>: Display if <n> is even or odd
    /states_list: Display the list of states

"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the current SQL Alchemy session aftr each request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a list of states from the storage engine
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
