#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask


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

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
