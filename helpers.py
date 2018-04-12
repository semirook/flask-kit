# coding: utf-8

"""
    helpers
    ~~~~~~~

    Implements useful helpers.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

import os

from flask import Flask
from werkzeug.utils import import_string


class NoContextProcessorException(Exception):
    pass


class NoBlueprintException(Exception):
    pass


class NoExtensionException(Exception):
    pass


class AppFactory(object):

    def __init__(self, config=None, envvar='PROJECT_SETTINGS'):
        self.app_config = config
        self.app_envvar = os.environ.get(envvar, 'settings.DevelopmentConfig')

    def get_app(self, app_module_name, **kwargs):
        self.app = Flask(app_module_name, **kwargs)
        if self.app_config:
            self.app.config.from_object(self.app_config)
        if self.app_envvar:
            self.app.config.from_object(self.app_envvar)

        self._bind_extensions()
        self._register_blueprints()
        self._register_context_processors()

        return self.app

    def _get_imported_stuff_by_path(self, path):
        module_name, object_name = path.rsplit('.', 1)
        module = import_string(module_name)

        return module, object_name

    def _bind_extensions(self):
        for ext_path in self.app.config.get('EXTENSIONS', []):
            module, e_name = self._get_imported_stuff_by_path(ext_path)
            if not hasattr(module, e_name):
                raise NoExtensionException(
                    'No {e_name} extension found'.format(e_name=e_name)
                )

            ext = getattr(module, e_name)
            if hasattr(ext, 'init_app'):
                ext.init_app(self.app)
            elif callable(ext):
                ext(self.app)
            else:
                raise NoExtensionException(
                    '{e_name} extension has no init_app. Can\'t initialize'.format(e_name=e_name)
                )

    def _register_context_processors(self):
        for processor_path in self.app.config.get('CONTEXT_PROCESSORS', []):
            module, p_name = self._get_imported_stuff_by_path(processor_path)
            if hasattr(module, p_name):
                self.app.context_processor(getattr(module, p_name))
            else:
                raise NoContextProcessorException(
                    'No {cp_name} context processor found'.format(cp_name=p_name)
                )

    def _register_blueprints(self):
        for blueprint_path in self.app.config.get('BLUEPRINTS', []):
            module, b_name = self._get_imported_stuff_by_path(blueprint_path)
            if hasattr(module, b_name):
                self.app.register_blueprint(getattr(module, b_name))
            else:
                raise NoBlueprintException(
                    'No {bp_name} blueprint found'.format(bp_name=b_name)
                )
