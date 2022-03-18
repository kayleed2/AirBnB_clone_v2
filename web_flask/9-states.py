#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = storage.all(State)
    inst = 0
    if id:
        for k, v in states.items():
            if id == v.id:
                inst = v
        return render_template('9-states.html',
                               states=states, id=id, inst=inst)
    elif id is None:
        return render_template('9-states.html', states=states, inst=inst)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
