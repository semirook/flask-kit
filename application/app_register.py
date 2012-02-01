# -*- coding: utf-8 -*-

"""
    app_register
    ~~~~~~~~~~~~

    Application initialization and registrations

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from application import app

# Register you database object or additional Flask plugins that require
# original app object here to avoid some problems with circular imports
from database import *

# Leave these methods at the end of the `app_register` module to avoid
# some problems with circular imports
app.register_all_blueprints()
app.register_all_context_processors()
