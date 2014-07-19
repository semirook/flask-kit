# -*- coding: utf-8 -*-

"""
    settings
    ~~~~~~~~

    Global settings for project.
"""
import os
from local_settings import LocalConfig

class BaseConfig(LocalConfig):
    ADMIN_PER_PAGE = 5
    CODEMIRROR_LANGUAGES = ['python','python2','python3','php','javascript','xml']
    CODEMIRROR_THEME = 'blackboard'#'vivid-chalk'#'3024-night'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

    URL_MODULES = [
            'base.urls.routes',
            'info.urls.routes',
            #'admin.urls.routes',
            #'auth.urls.routes',
            #'blog.urls.routes',
            #'member.urls.routes',
            #'page.urls.routes',
    ]

    BLUEPRINTS = [
            'base.base',
            'info.info',
            #'admin.admin',
            #'menu.menu',
            #'blog.blog',
            #'page.page',
            #'auth.auth',

    ]

    EXTENSIONS = [
            'ext.db',
            'ext.toolbar',
            #'ext.pagedown',
            #'ext.codemirror',
            #'ext.alembic',
    ]

    CONTEXT_PROCESSORS = [
            'base.context_processors.common_context',
            'base.context_processors.common_forms',
            #'menu.context_processors.frontend_nav',
            #'menu.context_processors.admin_nav',
            #'auth.context_processors.user_context',
            #'core.context_processors.add_is_page',
    ]

    TEMPLATE_FILTERS = [
            'base.filters.date',
            'base.filters.date_pretty',
            'base.filters.datetime',
            'base.filters.pluralize',
            'base.filters.month_name',
            'base.filters.markdown',
    ]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
