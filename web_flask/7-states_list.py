#!/usr/bin/python3
"""DFSGFDSGDFSGFDG DFGDF G"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """SDFDSF SDF SD FSDF SDF """
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(self):
    """SDSDFF SDFSD FSDF SDFSD"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
