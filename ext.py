# -*- coding: utf-8 -*-

"""
    ext
    ~~~

    Good place for pluggable extensions.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.gravatar import Gravatar
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment


db = SQLAlchemy()
assets = Environment()
login_manager = LoginManager()


# Almost any modern Flask extension has special init_app()
# method for deferred app binding. But there are a couple of
# popular extensions that no nothing about such use case.

gravatar = lambda app: Gravatar(app, size=50)  # has no init_app()
toolbar = lambda app: DebugToolbarExtension(app)  # has no init_app()
