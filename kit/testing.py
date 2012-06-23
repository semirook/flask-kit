# -*- coding: utf-8 -*-

"""
    testing
    ~~~~~~~

    Simple demo TestCase

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from flaskext.testing import TestCase
from kit.helpers import AppFactory
from settings import TestingConfig


class KitTestCase(TestCase):

    def create_app(self):
        return AppFactory(TestingConfig).get_app()
