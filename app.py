# coding: utf-8

"""
    application
    ~~~~~~~~~~~

    Application initialization
    and app-specific registrations.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.assets import Bundle
from ext import assets
from helpers import AppFactory


app = AppFactory().get_app(__name__)

css_base = Bundle(*app.config.get('CSS_BASE_BUNDLE', []), filters='cssmin', output='gen/base.css')
assets.register('css_base', css_base)

js_base = Bundle(*app.config.get('JS_BASE_BUNDLE', []), filters='jsmin', output='gen/base.js')
assets.register('js_base', js_base)
