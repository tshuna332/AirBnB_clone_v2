#!/usr/bin/python3
"""SDFSD FDS FSD FSDF """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def states():
    """Returns a html listing the states"""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def close(self):
    """ DSFSDF SDF SDFS SDF SDFS F """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
