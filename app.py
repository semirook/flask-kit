# -*- coding: utf-8 -*-

"""
    application
    ~~~~~~~~~~~

    Application initialization
    and app-specific registrations.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.assets import Bundle
from helpers import AppFactory
from settings import DevelopmentConfig
from ext import assets


app = AppFactory(DevelopmentConfig).get_app(__name__)


# Assets zone

css_base_bundle = ['css/reset.css', 'css/typo.css', 'css/style.css',
                   'css/page.css', 'css/forms.css']

css_base = Bundle(*css_base_bundle, filters='cssmin', output='gen/base.css')
assets.register('css_base', css_base)

js_base_bundle = ['js/libs/json2.js', 'js/libs/jquery-1.8.2-min.js',
                  'js/libs/underscore-1.4.2-min.js', 'js/libs/backbone-0.9.2-min.js']

js_base = Bundle(*js_base_bundle, filters='jsmin', output='gen/base.js')
assets.register('js_base', js_base)
