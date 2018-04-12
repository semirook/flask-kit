# coding: utf-8

"""
    ext
    ~~~

    Good place for pluggable extensions.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask_debugtoolbar import DebugToolbarExtension
from flask_gravatar import Gravatar
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment


db = SQLAlchemy()
assets = Environment()
login_manager = LoginManager()
gravatar = Gravatar(size=50)
toolbar = DebugToolbarExtension()

# Almost any modern Flask extension has special init_app()
# method for deferred app binding. But there are a couple of
# popular extensions that no nothing about such use case.
# Or, maybe, you have to use some app.config settings

# gravatar = lambda app: Gravatar(app, size=50)
