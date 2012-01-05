#!/usr/bin/env python
import sys
from kit.helpers import get_module


if __name__ == '__main__':
    global_settings = get_module('settings')
    common_module = getattr(global_settings, 'APP_MODULE', 'common')
    app_module = get_module('{0}.views'.format(common_module))
    app = getattr(app_module, 'app', False)
    if app:
        app.run()
    else:
        sys.stderr.write("Create main 'app' instance in '{0}.views' module first\n".format(common_module))
