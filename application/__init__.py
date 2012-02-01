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

# Application initialization and magic registrations
from app_register import *

# All of yours application logic
from views import *
