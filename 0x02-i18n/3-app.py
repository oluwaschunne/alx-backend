#!/usr/bin/env python3
"""0x02. i18n"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """ Config class for app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)

app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the locale of the application"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """default home page"""
    return render_template(
        "3-index.html",
    )


if __name__ == "__main__":
    app.run(debug=True)
