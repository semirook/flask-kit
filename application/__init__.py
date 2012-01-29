# -*- coding: utf-8 -*-

"""
    application
    ~~~~~~~~~~~

    Application initialization and registrations

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from kit.helpers import AppFactory
from settings import DevelopmentConfig


# It's your main flask app.
# You may define your own config class for it in settings.py
app = AppFactory(DevelopmentConfig).get_app()

# Your database object. It's important to define or import module with it here
# to be able to use it without circular problems all over the project
from database import *

# Very important is to register your blueprints and context processors
# from settings.py right here to avoid some problems with circular imports.
# :meth:`register_all_blueprints` and :meth:`register_all_context_processors`
# are additional methods from factory to make it for you
app.register_all_blueprints()
app.register_all_context_processors()


# All of yours application logic
from views import *
