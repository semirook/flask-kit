# coding: utf-8

"""
    ext
    ~~~

    Good place for pluggable extensions.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.gravatar import Gravatar
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from flask.ext.restplus import Api


db = SQLAlchemy()
assets = Environment()
login_manager = LoginManager()
gravatar = Gravatar(size=50)
toolbar = DebugToolbarExtension()
api = Api(default='api')

# Almost any modern Flask extension has special init_app()
# method for deferred app binding. But there are a couple of
# popular extensions that no nothing about such use case.
# Or, maybe, you have to use some app.config settings

# gravatar = lambda app: Gravatar(app, size=50)
