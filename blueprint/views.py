# -*- coding: utf-8 -*-
from blueprint import blueprint
from flask.templating import render_template
from flask.views import View


# Simple example of blueprint view
class SubscribePageView(View):
    def dispatch_request(self):
        return render_template('welcome_page.html')


# URL rules
blueprint.add_url_rule('/welcome', view_func=SubscribePageView.as_view('welcome_page'))
