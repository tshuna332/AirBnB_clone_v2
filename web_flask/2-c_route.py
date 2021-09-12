#!/usr/bin/python3
"""SAD DFFDSD DSFGSDFG"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """SFDFG DSDSF DFGFD"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """DDFSFDG FGDFGD FDG"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """FSDG SFDGDFSG sdfg"""
    res = text.replace("_", " ")
    return 'C {}'.format(res)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
