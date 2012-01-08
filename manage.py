#!/usr/bin/env python

"""
    manage
    ~~~~~~

    Set of useful management commands

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

import code
from flaskext.script import Manager, Shell, Command, Option
from kit.helpers import get_main_app, BlueprintPackageFactory


app = get_main_app()
manager = Manager(app)


class iShell(Shell):
    """Works with iPython >= 0.12"""

    def run(self, no_ipython):
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
        BlueprintPackageFactory(name).build()


manager.add_command("shell", iShell())
manager.add_command("createblueprint", Blueprint())


if __name__ == "__main__":
    manager.run()
