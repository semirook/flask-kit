# -*- coding: utf-8 -*-
from flask import Blueprint


base = Blueprint('base', __name__,
                 template_folder='templates',
                 url_prefix='/')


from views import *
