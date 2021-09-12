#!/usr/bin/python3
"""ADSFG SDFG SDFSD FSDF"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ASDSFDSDF SDF SD"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ASDFDS DFDSF SDF """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ASD DSFSDFSD FSDF"""
    res = text.replace("_", " ")
    return 'C {}'.format(res)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is_cool"):
    """ASD DFDFDSFDSF dsFDSF"""
    res = text.replace("_", " ")
    return 'Python {}'.format(res)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
