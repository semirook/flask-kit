# -*- coding: utf-8 -*-

"""
    context_processors
    ~~~~~~~~~~~~~~~~~~

    The set of context processors

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""


def my_contacts():
    """Very simple example of context processor"""
    return {'my_email': 'semirook@gmail.com',
            'my_github': 'https://github.com/semirook',
            }
