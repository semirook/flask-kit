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

# It's your main flask app instance
app = AppFactory(DevelopmentConfig).get_app()

# Leave this stuff here to avoid some problems with circular imports
app.register_blueprints()
app.register_context_processors()

from database import *
from views import *
