#!/usr/bin/python3
"""FDGHDGDHSSDFUGJSHD FSDFDSFU HSDFS"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_id(id=None):
    """FDJGDFG fdsGDG DFG FDG FD"""
    states = storage.all(State)
    if (id):
        return render_template('9-states.html', states=states, id=id)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close(self):
    """DFSGFDGFSDGDFSGSDFGSD FD SDF SDF DDF"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
