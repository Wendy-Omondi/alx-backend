#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template


app = flask(__name__)


@app.route('/')
def root():
    """flask app"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.tun()
