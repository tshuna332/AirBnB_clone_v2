#!/usr/bin/python3
"""ASDA FADSDADF"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """DFSFGS ADS SDFGDGSD"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """DFFDS SDF SDF S FD"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
