#!/usr/bin/env python
from flaskext.script import Manager
from kit.helpers import get_main_app


app = get_main_app()
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
