# -*- coding: utf-8 -*-

"""
    kit.helpers
    ~~~~~~~~~~~

    Implements Flaskit helpers.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import importlib
import settings
import os

from flask import Flask
from werkzeug.utils import find_modules

from .exceptions import NoAppException, NoBlueprintException, NoContextProcessorException
from .templates.blueprint import (BLUEPRINT_VIEWS_TEMPLATE,
                                  BLUEPRINT_INIT_TEMPLATE,
                                  BLUEPRINT_MODELS_TEMPLATE)


class ModulesHelper(object):
    """
    The set of methods that used by another helpers and can be used
    by yourself for some operations with modules import and existence check
    """

    def __init__(self, module_name):
        self.module_name = module_name

    def is_module_exists(self):
        """
        Checks if module exists by the module name as the parameter:

               is_module_exist('app.views')

        Throws the error string to the console output if no module found
        but doesn't raise any exception. Returns bool value.
        """
        try:
            find_modules(self.module_name)
            return True
        except ImportError:
            return False

    def get_module(self):
        """
        Returns the imported module object by the module name as the parameter:

               get_module('app.views')

        Doesn't raise any exception if no module found (will return `False` in such case).
        """
        if self.is_module_exists():
            return importlib.import_module(self.module_name)


class MainAppHelper(object):

    @classmethod
    def get_app(cls):
        """
        Returns the `app` instance from the module specified in the APP_PACKAGE
        attribute in your settings.py.
        """
        app_module_name = getattr(settings, 'APP_PACKAGE', False)
        if not app_module_name:
            raise NoAppException('Define APP_PACKAGE in settings.py')

        app_module = ModulesHelper(app_module_name).get_module()
        app_instance = getattr(app_module, 'app', False)
        if not app_instance:
            raise NoAppException('No app instance found in "{mod}" module'.format(mod=app_module.__name__))

        return app_instance


class AppFactory(object):
    """
    Flaskit application factory. It's really simple to use:

           app = AppFactory(DevelopmentConfig).get_app()

    :param DevelopmentConfig: your config class for this app instance from settings.py

    :meth:`get_app` is the basic method to make new app instance with registered
    blueprints and context processors.
    """

    def __init__(self, config, envvar='PROJECT_SETTINGS'):
        self.app_config = config
        self.app_envvar = envvar

    def get_app(self, app_module_name=None, **kwargs):
        app_module_name = app_module_name or getattr(settings, 'APP_PACKAGE', False)
        self.app = self._get_new_app_instance(app_module_name, **kwargs)
        self.app.register_blueprints = self._register_blueprints
        self.app.register_context_processors = self._register_context_processors

        return self.app

    def _get_new_app_instance(self, app_module_name, **kwargs):
        new_app = Flask(app_module_name, **kwargs)
        new_app.config.from_envvar(self.app_envvar, silent=True)
        new_app.config.from_object(self.app_config)

        return new_app

    def _register_context_processors(self):
        processors = getattr(settings, 'CONTEXT_PROCESSORS', [])
        for processor in processors:
            processor_module_name = '.'.join(processor.split('.')[:-1])
            processor_itself_name = processor.split('.')[-1]
            module = ModulesHelper(processor_module_name).get_module()
            if module and hasattr(module, processor_itself_name):
                self.app.context_processor(getattr(module, processor_itself_name))
            else:
                raise NoContextProcessorException()

    def _register_blueprints(self):
        blueprints = getattr(settings, 'INSTALLED_BLUEPRINTS', [])
        for bp_name in blueprints:
            bp_package = ModulesHelper(bp_name).get_module()
            if hasattr(bp_package, bp_name):
                self.app.register_blueprint(getattr(bp_package, bp_name))

            else:
                raise NoBlueprintException()


class BlueprintsFactory(object):
    """
    Creates new blueprint package by the set of templates.
    Used by management-command `createblueprint`
    """

    def __init__(self, name, structure=None):
        self.base_dir = os.path.abspath(os.path.dirname(settings.__file__))
        self.blueprint_name = name
        self.blueprint_dir = os.path.join(self.base_dir, self.blueprint_name)
        self.blueprint_structure = structure or \
                                   {'__init__.py': BLUEPRINT_INIT_TEMPLATE,
                                    'models.py': BLUEPRINT_MODELS_TEMPLATE,
                                    'views.py': BLUEPRINT_VIEWS_TEMPLATE,
                                    '/templates': None,
                                    '/static': None,
                                    }

    def make_file(self, template, path):
        new_file = template.render(**self.__dict__)
        with open(path, "w") as file_obj:
            file_obj.write(new_file)

    def make_dir(self, *args):
        if not args:
            if os.path.exists(self.blueprint_dir):
                raise RuntimeError("You already have a package with this name")
            else:
                os.makedirs(self.blueprint_dir)
        elif args:
            full_path = os.path.join(self.blueprint_dir, *args)
            os.makedirs(full_path)

    def build(self):
        self.make_dir()
        for file_or_folder, template in self.blueprint_structure.items():
            if not template and file_or_folder.startswith('/'):
                self.make_dir(file_or_folder.strip('/'))
            else:
                self.make_file(template, os.path.join(self.blueprint_dir, file_or_folder))
