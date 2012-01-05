# -*- coding: utf-8 -*-

"""
    Implements some additional kit helpers.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import imp
import importlib
import sys


NO_MODULE_COMMON_ERROR = """Error: Can't find module {0} and can't work around this error\n"""

NO_SETTINGS_ERROR = """Error: Can't find the file 'settings.py' in the directory containing {0}.
It's common for the whole project, so you have to create it\n""".format(__file__)

NO_KIT_ERROR = """Error: Can't find 'kit' module, which provides some necessary helpers\n"""


def is_module_exist(module_name):
    error_map = {'settings': NO_SETTINGS_ERROR,
                 'kit': NO_KIT_ERROR,
                 }
    try:
        imp.find_module(module_name.replace('.', '/'))
        return True
    except ImportError:
        if module_name in error_map.keys():
            sys.stderr.write(error_map[module_name])
        else:
            sys.stderr.write(NO_MODULE_COMMON_ERROR.format(module_name))
        return False


def get_module(module_name):
    if is_module_exist(module_name):
        return importlib.import_module(module_name)
