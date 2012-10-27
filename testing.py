# -*- coding: utf-8 -*-

"""
    testing
    ~~~~~~~

    More useful TestCase for tests.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.testing import TestCase
from helpers import AppFactory
from settings import TestingConfig
from ext import db


class KitTestCase(TestCase):

    def create_app(self):
        return AppFactory(TestingConfig).get_app(__name__)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
