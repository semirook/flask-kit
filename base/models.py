# coding: utf-8

"""
    base.models
    ~~~~~~~~~~~

    The most common models for the whole project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db


class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        if any(
            (
                isinstance(id, str) and id.isdigit(),
                isinstance(id, (int, float))
            ),
        ):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


class User(UserMixin, CRUDMixin, db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return u'<User %r>' % self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
