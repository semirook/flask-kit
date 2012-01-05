# -*- coding: utf-8 -*-

"""
    Implements some base kit helpers.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""


__version__ = '0.1'

import importlib
import settings
from flask import Flask


class AppFactory(object):
    """Flask application factory. It's really simple to use:

           app = AppFactory(DevelopmentConfig).get_app()

    :param DevelopmentConfig: your config class for this app instance from settings.py

    :meth:`get_app` is the basic method to receive new app instance
    with registered blueprints (INSTALLED_BLUEPRINTS list, by default) and automatically calls
    :meth:`register_blueprints` by design.

    If you don't want to register any blueprints and want to get simple basic app,
    there is :meth:`get_blank_app` for you:

           app = AppFactory(DevelopmentConfig).get_blank_app()

    """
    def __init__(self, config, envvar='PROJECT_SETTINGS'):
        self.app = Flask(self.get_import_name())
        self.app.config.from_object(config)
        self.app.config.from_envvar(envvar, silent=True)

    def get_import_name(self):
        app_module = self._get_app_module()
        try:
            module = importlib.import_module('{0}.views'.format(app_module))
            return module.__name__
        except ImportError:
            raise Exception("Main logic module '{0}.views' not found".format(app_module))

    def get_blank_app(self):
        return self.app

    def get_app(self):
        self.register_blueprints()
        return self.app

    def register_blueprints(self):
        blueprints = self._get_installed_blueprints()
        if blueprints:
            self._bind_blueprints_to_app(blueprints)

    def _get_installed_blueprints(self):
        return getattr(settings, 'INSTALLED_BLUEPRINTS', False)

    def _get_app_module(self):
        return getattr(settings, 'APP_MODULE', 'app')

    def _bind_blueprints_to_app(self, blueprints):
        for bp_name in blueprints:
            try:
                bp_logic = importlib.import_module('{0}.views'.format(bp_name))
                bp_obj = getattr(bp_logic, bp_name, False)
                if bp_obj:
                    self.app.register_blueprint(bp_obj)
                else:
                    raise Exception("No '{0}' blueprint object found in {1}".format(bp_name, bp_logic.__name__))
            except ImportError:
                raise Exception("'{0}' blueprint module registered in settings.py but not found".format(bp_name))
