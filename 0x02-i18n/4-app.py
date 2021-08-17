#!/usr/bin/env python3
"""Get ocale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determines the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """flask app"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.tun()
