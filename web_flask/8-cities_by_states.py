#!/usr/bin/python3
"""SDFSD FDS FSD FSDF """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """ DFGDFG DFG FDG FDG DFG DDFG """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    """ DSFSDF SDF SDFS SDF SDFS F """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
