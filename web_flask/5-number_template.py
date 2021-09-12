#!/usr/bin/python3
"""SD FSFDSDFDS FSDF SDF DS"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """DFSSDFG DDFSDF SDF SDFDS"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """SDFDF GFG DFG DF GDF"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """DSFDSFSDFS DFSDF SDFDS"""
    res = text.replace("_", " ")
    return 'C {}'.format(res)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is_cool"):
    """SDFSD FDSDFS DFSDF S"""
    res = text.replace("_", " ")
    return 'Python {}'.format(res)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ADSFDS FDFS DFSD FS"""
    return '{:d} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """DFSGFD DFDFGDFDF DFGDFG"""
    return render_template("5-number.html", var=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
