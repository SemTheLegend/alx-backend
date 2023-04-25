#!/usr/bin/env python3
"""Basic Flask App with Basic Babel Setup."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(app):
    """Contains a list of languages."""
    LANGUAGES = ["en", "fr"]
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def home():
    """Returns the home page."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
