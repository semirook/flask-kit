# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint
from flask.templating import render_template
from flask.views import View


# It is a very simple example of the very simple blueprint.
# Blueprint encapsulates some logic, models, urls, templates etc. to keep
# your main app clean and simple to maintain.
# If you are not familiar with the concept of blueprints - please, visit
# http://flask.pocoo.org/docs/blueprints/
blueprint = Blueprint('blueprint', __name__, template_folder='templates')


# So, write some views
class SubscribePageView(View):
    def dispatch_request(self):
        return render_template('welcome_page.html')


# And add some view URL rules to the blueprint
blueprint.add_url_rule('/welcome', view_func=SubscribePageView.as_view('welcome_page'))
