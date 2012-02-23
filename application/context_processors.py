# -*- coding: utf-8 -*-

"""
    context_processors
    ~~~~~~~~~~~~~~~~~~

    The set of context processors

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

# Very simple example of context processor.
# You can use `my_email` variable in your templates
def my_email():
    return {'my_email': 'semirook@ya.ru'}
