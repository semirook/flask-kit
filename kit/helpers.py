# -*- coding: utf-8 -*-

"""
    kit.helpers
    ~~~~~~~~~~~

    Implements some basic kit helpers.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import importlib
import sys
import settings
import os
from flask import Flask
from werkzeug.utils import find_modules
from .templates.blueprint import (BLUEPRINT_VIEWS_TEMPLATE,
                                  BLUEPRINT_INIT_TEMPLATE,
                                  BLUEPRINT_MODELS_TEMPLATE)


NO_MODULE_COMMON_ERROR = "Can't find module {0}"

NO_OBJECT_COMMON_ERROR = "No '{0}' object found in {1}"

NO_SETTINGS_ERROR = """Can't find the file 'settings.py' in the directory containing {0}.
It's common for the whole project, so you have to create it""".format(__file__)

NO_MAIN_APP_INSTANCE_ERROR = "Can't find or can't import the main 'app' instance in '{0}'"

NO_APP_PACKAGE_ATTRIBUTE_ERROR = "Define the APP_PACKAGE settings attribute, please"

NO_REGISTERED_MODULE_ERROR = "'{0}' module registered in settings.py but not found"

NO_REGISTERED_CONTEXT_PROCESSOR_ERROR = "'{0}' context processor registered in settings.py but not found"


class ModulesHelper(object):
    def __init__(self, module_name):
        self.module_name = module_name

    def is_module_exist(self):
        """Checks if module exists by the module name as the parameter:

               is_module_exist('app.views')

        Throws the error string to the console output if no module found
        but doesn't raise any exception. Returns bool value.
        """
        error_map = {'settings': NO_SETTINGS_ERROR}
        try:
            find_modules(self.module_name)
            return True
        except ImportError:
            if self.module_name in error_map.keys():
                sys.stderr.write(error_map[self.module_name])
            else:
                sys.stderr.write(NO_MODULE_COMMON_ERROR.format(self.module_name))
            return False

    def get_module(self):
        """Returns the imported module object by the module name as the parameter:

               get_module('app.views')

        Doesn't raise any exception if no module found (will return `False` in such case).
        """
        if self.is_module_exist():
            return importlib.import_module(self.module_name)


class MainAppHelper(object):

    @classmethod
    def get_instance(cls):
        """Returns the `app` instance from the module specified in the APP_PACKAGE
        attribute in your settings.py. Raises ImportError if no app instance found.
        """
        app_module_name = cls.get_module_name()
        app_module = ModulesHelper(app_module_name).get_module()

        if hasattr(app_module, 'app'):
            return getattr(app_module, 'app', False)
        else:
            raise ImportError(NO_MAIN_APP_INSTANCE_ERROR.format(app_module_name))

    @classmethod
    def get_module_name(cls):
        """Returns the main `app` module name `package_name`, where
        package_name is APP_PACKAGE attribute from your settings.py.
        Raises AttributeError if no APP_PACKAGE attribute found.
        """
        app_package_name = getattr(settings, 'APP_PACKAGE', False)
        if app_package_name:
            return app_package_name
        else:
            raise AttributeError(NO_APP_PACKAGE_ATTRIBUTE_ERROR.format(app_package_name))


class AppFactory(object):
    """Flask application factory. It's really simple to use:

           app = AppFactory(DevelopmentConfig).get_app()

    :param DevelopmentConfig: your config class for this app instance from settings.py

    :meth:`get_app` is the basic method to receive new app instance
    with registered blueprints from the INSTALLED_BLUEPRINTS list
    and registered context processors from the CONTEXT_PROCESSORS list
    from settings.py
    """
    def __init__(self, config, envvar='PROJECT_SETTINGS'):
        self.app_config = config
        self.app_envvar = envvar

    def get_app(self, import_name=None, **kwargs):
        self.app = self._get_new_app_instance(import_name, **kwargs)
        self.app.register_all_blueprints = self._register_blueprints
        self.app.register_all_context_processors = self._register_context_processors

        return self.app

    def _get_new_app_instance(self, import_name, **kwargs):
        if not import_name:
            import_name = MainAppHelper.get_module_name()
        new_app = Flask(import_name, **kwargs)
        new_app.config.from_object(self.app_config)
        new_app.config.from_envvar(self.app_envvar, silent=True)

        return new_app

    def _register_context_processors(self):
        if hasattr(settings, 'CONTEXT_PROCESSORS'):
            processors = getattr(settings, 'CONTEXT_PROCESSORS')
            for processor in processors:
                processor_module_name = '.'.join(processor.split('.')[:-1])
                processor_itself_name = processor.split('.')[-1]
                module = ModulesHelper(processor_module_name).get_module()
                if module and hasattr(module, processor_itself_name):
                    self.app.context_processor(getattr(module, processor_itself_name))
                else:
                    raise ImportError(NO_REGISTERED_CONTEXT_PROCESSOR_ERROR.format(processor))

    def _register_blueprints(self):
        if hasattr(settings, 'INSTALLED_BLUEPRINTS'):
            blueprints = getattr(settings, 'INSTALLED_BLUEPRINTS')
            for bp_name in blueprints:
                bp_module = ModulesHelper(bp_name).get_module()
                if not bp_module:
                    raise ImportError(NO_REGISTERED_MODULE_ERROR.format(bp_name))
                if hasattr(bp_module, bp_name):
                    self.app.register_blueprint(getattr(bp_module, bp_name))
                else:
                    raise AttributeError(NO_OBJECT_COMMON_ERROR.format(bp_name, bp_module.__name__))


class BlueprintPackageFactory(object):
    """Creates new blueprint package by the set of templates.
    Used by management-command `createblueprint`"""

    def __init__(self, blueprint_name):
        self.base_dir = os.path.abspath(os.path.dirname(settings.__file__))
        self.blueprint_name = blueprint_name
        self.blueprint_dir = os.path.join(self.base_dir, self.blueprint_name)
        self.blueprint_structure = {'__init__.py': BLUEPRINT_INIT_TEMPLATE,
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
        for file_or_folder, template_or_type in self.blueprint_structure.items():
            if not template_or_type and file_or_folder.startswith('/'):
                self.make_dir(file_or_folder.strip('/'))
            else:
                self.make_file(template_or_type, os.path.join(self.blueprint_dir, file_or_folder))
