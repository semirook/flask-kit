# coding: utf-8

"""
    base.forms
    ~~~~~~~~~~

    The most common forms for the whole project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Email, Required


class LoginForm(FlaskForm):
    email = TextField('Login', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
