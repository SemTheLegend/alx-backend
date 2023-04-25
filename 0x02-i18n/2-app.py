#!/usr/bin/env python3
"""Basic Flask App with Basic Babel Setup."""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)


class Config():
    """Contains a list of languages."""
    LANGUAGES = ["en", "fr"]


@babel.localeselector
def get_locale():
    """Determines the best match for our supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """Returns the home page."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
