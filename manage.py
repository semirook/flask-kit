#!/usr/bin/env python
from flaskext.script import Manager, Shell
from kit.helpers import get_main_app
import code


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


manager.add_command("shell", iShell())


if __name__ == "__main__":
    manager.run()
