#!/usr/bin/env python

"""
    manage
    ~~~~~~

    Set of some useful management commands

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import code
from flaskext.script import Manager, Shell, Command, Option
from kit.helpers import MainAppHelper, BlueprintsFactory


app = MainAppHelper.get_app()
manager = Manager(app)


class iShell(Shell):
    """Works with iPython >= 0.12"""

    def run(self, no_ipython=False):
        context = self.get_context()
        if not no_ipython:
            try:
                from IPython.frontend.terminal.embed import InteractiveShellEmbed
                ipython_shell = InteractiveShellEmbed()
                return ipython_shell(global_ns=dict(), local_ns=context)
            except ImportError:
                pass

        code.interact(self.banner, local=context)


class Blueprint(Command):
    """Creates new blueprint package with the specified name"""

    def get_options(self):
        return [Option('-n', '--name', dest='name', required=True)]

    def run(self, name):
        BlueprintsFactory(name).build()


class NoseTests(Command):
    """Nose test runner"""

    def run(self):
        try:
            import nose
            nose.run(argv=['nosetests'])
        except ImportError:
            pass


manager.add_command("shell", iShell())
manager.add_command("createblueprint", Blueprint())
manager.add_command("test", NoseTests())


if __name__ == "__main__":
    manager.run()
