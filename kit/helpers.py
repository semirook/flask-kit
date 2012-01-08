# -*- coding: utf-8 -*-

"""
    kit.helpers
    ~~~~~~~~~~~

    Implements some basic kit helpers.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import imp
import importlib
import sys
from flask import Flask
import settings


NO_MODULE_COMMON_ERROR = "Can't find module {0}"

NO_OBJECT_COMMON_ERROR = "No '{0}' object found in {1}"

NO_SETTINGS_ERROR = """Can't find the file 'settings.py' in the directory containing {0}.
It's common for the whole project, so you have to create it""".format(__file__)

NO_MAIN_APP_INSTANCE_ERROR = "Can't find or can't import the main 'app' instance in '{0}'"

NO_APP_PACKAGE_ATTRIBUTE_ERROR = "Define the APP_PACKAGE settings attribute, please"

NO_REGISTERED_MODULE_ERROR = "'{0}' module registered in settings.py but not found"


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
    """Returns the `app` instance from the module specified in the APP_PACKAGE
    attribute in your settings.py. Raises exception if no app instance found.
    """
    app_module_name = get_main_app_module_name()
    app_module = get_module(app_module_name)

    if hasattr(app_module, 'app'):
        return getattr(app_module, 'app', False)
    else:
        raise ImportError(NO_MAIN_APP_INSTANCE_ERROR.format(app_module_name))


def get_main_app_module_name():
    """Returns the main `app` module name `package_name.views`, where
    package_name is APP_PACKAGE attribute from your settings.py
    """
    app_package_name = getattr(settings, 'APP_PACKAGE', False)
    if app_package_name:
        return '{package}.views'.format(package=app_package_name)
    else:
        raise AttributeError(NO_APP_PACKAGE_ATTRIBUTE_ERROR.format(app_package_name))


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

    def get_blank_app(self, import_name=None, **kwargs):
        return self._get_new_app_instance(import_name, **kwargs)

    def get_app(self, import_name=None, **kwargs):
        app = self._get_new_app_instance(import_name, **kwargs)
        self._register_blueprints(app)

        return app

    def _get_new_app_instance(self, import_name, **kwargs):
        if not import_name:
            import_name = get_main_app_module_name()
        new_app = Flask(import_name, **kwargs)
        new_app.config.from_object(self.app_config)
        new_app.config.from_envvar(self.app_envvar, silent=True)

        return new_app

    def _register_blueprints(self, app):
        if hasattr(settings, 'INSTALLED_BLUEPRINTS'):
            blueprints = getattr(settings, 'INSTALLED_BLUEPRINTS')
            for bp_name in blueprints:
                bp_module = get_module('{package}.views'.format(package=bp_name))
                if not bp_module:
                    raise ImportError(NO_REGISTERED_MODULE_ERROR.format(bp_name))
                if hasattr(bp_module, bp_name):
                    app.register_blueprint(getattr(bp_module, bp_name))
                else:
                    raise AttributeError(NO_OBJECT_COMMON_ERROR.format(bp_name, bp_module.__name__))
