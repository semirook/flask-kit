# -*- coding: utf-8 -*-
from flask_kit.helpers import AppFactory
from flask_kit.settings import DevelopmentConfig


# It's your main flask app.
# You may define your own config class for it in settings.py
app = AppFactory(DevelopmentConfig).get_app()


# Your main views may be here. In fact, all of your views may be here
# if you don't use blueprints and your site is really micro.
