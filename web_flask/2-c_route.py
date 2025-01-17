#!/usr/bin/python3
""" Defines the message on the /c page """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns the message for the index"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns the message for /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def message(text):
    """Returns a custom message"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
