# coding: utf-8

"""
    base.tests
    ~~~~~~~~~~

    Example tests.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask import url_for
from .test_case import KitTestCase


class TestFrontBlueprint(KitTestCase):

    def test_front(self):
        response = self.client.get(url_for('base.front_page'))
        self.assert200(response)

    def test_front_for_anonymous(self):
        response = self.client.get(url_for('base.front_page'))
        self.assertContains(response, 'Log in')

    def test_login(self):
        response = self.client.get(url_for('base.login'))
        self.assert200(response)
