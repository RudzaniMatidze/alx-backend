#!/usr/bin/env python3
"""
Simple Flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Represents a Flask Babelconfiguration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.rout('/')
def get_index() -> str:
    """
    The home/index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
