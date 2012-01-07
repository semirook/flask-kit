# -*- coding: utf-8 -*-

"""
    Global settings for whole project.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

class BaseConfig(object):
    """Base config class"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Optional config for development needs.
    Make your own like this, inherit from BaseConfig class.
    """
    DEBUG = True
    TESTING = True


# You may decide to rename your main application module (app -> common, for example).
# Set it's name here ('app' is default)

APP_MODULE = 'app'


# If you will use some blueprints in your project (and you have to),
# register them in INSTALLED_BLUEPRINTS list.
# For example, if you have blueprint object like
# simple_page = Blueprint('simple_page', __name__)
# in the simple_page blueprint module, put it's name, not the imported object itself,
# in INSTALLED_BLUEPRINTS list -> INSTALLED_BLUEPRINTS = ['simple_page']

INSTALLED_BLUEPRINTS = ['blueprint']
