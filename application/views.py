# -*- coding: utf-8 -*-
from flask.templating import render_template
from flask.views import View
from application import app


# Your main views may be here. In fact, all of your views may be here
# if you don't use blueprints and your site is really micro.

# In this example we use so called `Pluggable Views` or `Class Based Views`.
# You should be familiar with them if you already had some experience with Django.
# If not - please, visit http://flask.pocoo.org/docs/views/
class MainPageView(View):
    def dispatch_request(self):
        return render_template('main.html')


# Good style is to place your view URL rules right after the view definition.
app.add_url_rule('/', view_func=MainPageView.as_view('main_page'))
