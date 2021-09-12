#!/usr/bin/python3
"""ASDAS ASDFASFDA"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ASD ASD ASD ASDAS D"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
