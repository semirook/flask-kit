# -*- coding: utf-8 -*-

"""
    Implements some basic kit helpers.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import imp
import importlib
import sys
from flask import Flask
import settings


NO_MODULE_COMMON_ERROR = """Error: Can't find module {0} and can't work around this error\n"""

NO_SETTINGS_ERROR = """Error: Can't find the file 'settings.py' in the directory containing {0}.
It's common for the whole project, so you have to create it\n""".format(__file__)


def is_module_exist(module_name):
    """Checks if module exists by the module name as the parameter:

           is_module_exist('app.views')

    Throws the error string to the console output if no module found
    but doesn't raise any exception. Returns bool value.
    """
    error_map = {'settings': NO_SETTINGS_ERROR}
    try:
        imp.find_module(module_name.replace('.', '/'))
        return True
    except ImportError:
        if module_name in error_map.keys():
            sys.stderr.write(error_map[module_name])
        else:
            sys.stderr.write(NO_MODULE_COMMON_ERROR.format(module_name))
        return False


def get_module(module_name):
    """Returns the imported module object by the module name as the parameter:

           get_module('app.views')

    Doesn't raise any exception if no module found (will return `False` in such case).
    """
    if is_module_exist(module_name):
        return importlib.import_module(module_name)


def get_main_app():
    """Special version of the `get_module` helper function.
    Returns the `app` instance from the app `views` module.
    Raises exception if no app instance found.
    """
    app_module_name = getattr(settings, 'APP_MODULE', 'app')
    app_module = get_module('{0}.views'.format(app_module_name))
    app_obj = getattr(app_module, 'app', False)
    if app_obj:
        return app_obj
    else:
        raise Exception("Can't find or can't import the main 'app' instance".format(app_module_name))


class AppFactory(object):
    """Flask application factory. It's really simple to use:

           app = AppFactory(DevelopmentConfig).get_app()

    :param DevelopmentConfig: your config class for this app instance from settings.py

    :meth:`get_app` is the basic method to receive new app instance
    with automatically registered blueprints from the INSTALLED_BLUEPRINTS list (from your settings.py)

    If you don't want to register any blueprints and want to get simple basic app,
    there is :meth:`get_blank_app` for you:

           app = AppFactory(DevelopmentConfig).get_blank_app()

    """
    def __init__(self, config, envvar='PROJECT_SETTINGS'):
        self.app_config = config
        self.app_envvar = envvar

    def get_app_import_name(self):
        app_import_name = getattr(settings, 'APP_MODULE', 'app')
        app_module = get_module('{0}.views'.format(app_import_name))
        if app_module:
            return app_module.__name__
        else:
            raise Exception("Main app module '{0}.views' not found".format(app_module))

    def get_blank_app(self, *args, **kwargs):
        return self._get_new_app_instance(*args, **kwargs)

    def get_app(self, *args, **kwargs):
        app = self._get_new_app_instance(*args, **kwargs)
        self._register_blueprints(app)

        return app

    def _get_new_app_instance(self, *args, **kwargs):
        new_app = Flask(self.get_app_import_name(), *args, **kwargs)
        new_app.config.from_object(self.app_config)
        new_app.config.from_envvar(self.app_envvar, silent=True)

        return new_app

    def _register_blueprints(self, app):
        blueprints = getattr(settings, 'INSTALLED_BLUEPRINTS', False)
        if blueprints:
            self._bind_blueprints_to_app(blueprints, app)

    def _bind_blueprints_to_app(self, blueprints, app):
        for bp_module_name in blueprints:
            bp_module = get_module('{0}.views'.format(bp_module_name))
            if not bp_module:
                raise Exception("'{0}' module registered in settings.py but not found".format(bp_module_name))
            bp_obj = getattr(bp_module, bp_module_name, False)
            if bp_obj:
                app.register_blueprint(bp_obj)
            else:
                raise Exception("No '{0}' object found in {1}".format(bp_module_name, bp_module.__name__))
