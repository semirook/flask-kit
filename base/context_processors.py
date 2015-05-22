# coding: utf-8

"""
    base.context_processors
    ~~~~~~~~~~~~~~~~~~~~~~~

    The most common context processors
    for the whole project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask.helpers import url_for
from base import LoginForm
from ext import gravatar


def common_context():
    return {
        'gravatar': gravatar,
        'my_email': 'semirook@gmail.com'
    }


def navigation():
    main_page = {
        'name': 'Main',
        'url': url_for('base.front_page'),
    }
    projects_page = {
        'name': 'Help',
        'url': url_for('info.help'),
    }

    return {'navigation': (main_page, projects_page)}


def common_forms():
    return {'login_form': LoginForm()}
