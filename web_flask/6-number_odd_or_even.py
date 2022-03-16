#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    new = text.replace("_", " ")
    return 'C %s' % new


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text=None):
    if text:
        if text is not None:
            new = text.replace("_", " ")
            return 'Python %s' % new
    else:
        return 'Python %s' % "is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    if (n % 2) == 0:
        oe = "even"
    else:
        oe = "odd"
    return render_template('6-number_odd_or_even.html', n=n, oe=oe)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)