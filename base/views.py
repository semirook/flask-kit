# -*- coding: utf-8 -*-

"""
    base.views
    ~~~~~~~~~~

    The most common views for the whole project.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

from flask.templating import render_template
from flask.views import MethodView
from flask import flash, redirect, request, url_for
from flask.ext.login import login_user, login_required, logout_user
from ext import login_manager
from base import base
from base.forms import LoginForm
from base.models import User


class FrontView(MethodView):

    def get(self):
        return render_template('base/main.html')



class LoginView(MethodView):
    _messages = {'success': 'You are the boss!',
                 'invalid_auth': 'Who are you?',
                 'invalid_form': 'Invalid form.',
                 }

    def get(self):
        return render_template('login.html', form=LoginForm())

    def post(self):
        form = LoginForm()
        if not form.validate_on_submit():
            flash(self._messages['invalid_form'])
            return render_template('login.html', form=form)

        user = User.get_by_email(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(self._messages['success'])
        else:
            flash(self._messages['invalid_auth'])
            return redirect(url_for('base.login'))

        return redirect(request.args.get('next') or url_for('base.front_page'))



login_manager.login_view = 'base.login'
login_manager.login_message = 'You have to log in to access this page.'


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@login_required
def logout():
    logout_user()
    return redirect(url_for('base.front_page'))

