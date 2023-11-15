#!/usr/bin/python3
"""Start Flask App, Cities by states"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page with a list of states and cities"""
    if type(storage).__name__ == "DBStorage":
        states = storage.all(State).values()
    else:
        states = storage.all("State").values()

    for state in states:
        if type(storage).__name__ == "DBStorage":
            state.cities = state.cities
        else:
            state.cities = state.cities()

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
