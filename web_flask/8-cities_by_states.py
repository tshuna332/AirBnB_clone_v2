#!/usr/bin/python3
"""DSFGSFDG FDGSDFGDSFD"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """DFSGSFSD FSDF SDF SDFS"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    """SDDFGDFGF SDFSDFSDFSDF SDFS"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

