#!/usr/bin/python3
""" Starting Flask App, State list """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all("State").values()
    states_list_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_list_sorted)


@app.teardown_appcontext
def close_db(error):
    """Closes storage engine at the end of the request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
