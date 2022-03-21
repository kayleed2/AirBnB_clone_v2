#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
