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

# It's your main flask app. Define your own config class in settings.py
app = AppFactory(DevelopmentConfig).get_app()

# Leave these imports here to avoid some problems with circular imports
from database import *

# Leave these methods here to avoid some problems with circular imports
app.register_all_blueprints()
app.register_all_context_processors()

# Application's views
from views import *
