#!/usr/bin/env python
import sys
from flask_kit import settings
from flask_kit.helpers import get_module


if __name__ == '__main__':
    common_module = getattr(settings, 'APP_MODULE', 'app')
    app_module = get_module('{0}.views'.format(common_module))
    app = getattr(app_module, 'app', False)
    if app:
        app.run()
    else:
        sys.stderr.write("Create main 'app' instance in '{0}.views' module first\n".format(common_module))
