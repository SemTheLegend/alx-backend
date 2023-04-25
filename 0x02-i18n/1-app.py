#!/usr/bin/env python3
"""Basic Flask App with Basic Babel Setup."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Contains a list of languages."""
    LANGUAGES = ["en", "fr"]
    
    
@app.route('/')
def home():
    """Returns the home page."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
 
