# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint


# Blueprint encapsulates some logic, models, urls, templates etc. to keep
# your main app clean and simple to maintain.

# If you are not familiar with the concept of blueprints - please, visit
# http://flask.pocoo.org/docs/blueprints/
blueprint = Blueprint('blueprint', __name__,
                      template_folder='templates',
                      static_folder='static',
                      url_prefix='/blueprint')


# Blueprint's views
from views import *
