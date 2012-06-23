# -*- coding: utf-8 -*-

"""
    kit.exceptions
    ~~~~~~~~~~~~~~

    The set of common Flaskit-specific exceptions.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""


class NoModuleException(Exception):
    pass


class NoSettingsException(Exception):
    pass


class NoAppException(Exception):
    pass


class NoContextProcessorException(Exception):
    pass


class NoBlueprintException(Exception):
    pass
