# coding: utf-8
from flask import Blueprint


info = Blueprint(
    'info', __name__,
    template_folder='templates',
    url_prefix='/info'
)


from .views import *
