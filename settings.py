# coding: utf-8

"""
    settings
    ~~~~~~~~

    Global settings for project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "MY_VERY_SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

    BLUEPRINTS = [
        'base.base',
        'info.info',
    ]

    EXTENSIONS = [
        'ext.db',
        'ext.assets',
        'ext.login_manager',
        'ext.gravatar',
        'ext.toolbar',
        # If you want Flask-RESTPlus out of the box
        # 'ext.api',
    ]

    CONTEXT_PROCESSORS = [
        'base.context_processors.common_context',
        'base.context_processors.navigation',
        'base.context_processors.common_forms',
    ]

    CSS_BASE_BUNDLE = [
        'css/reset.css',
        'css/typo.css',
        'css/style.css',
        'css/page.css',
        'css/forms.css',
    ]

    JS_BASE_BUNDLE = [
        'js/libs/jquery-1.11.3.js',
        'js/libs/underscore-1.8.3.js',
        'js/libs/backbone-1.2.0.js',
    ]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
