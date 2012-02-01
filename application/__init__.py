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

# Register you database object or additional Flask plugins that require
# original app object here to avoid some problems with circular imports
from database import *

# Leave these methods here to avoid some problems with circular imports
app.register_all_blueprints()
app.register_all_context_processors()

# All of yours application logic
from views import *
