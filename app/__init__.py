#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouyiran'
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.babel import lazy_gettext
from flask.json import JSONEncoder
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIN_PASSWORD
from momentjs import MomentJs

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))
mail = Mail(app)
babel = Babel(app)
lm.login_message = lazy_gettext('Please log in to access this page.')
app.jinja_env.globals['momentjs'] = MomentJs

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIN_PASSWORD:
        credentials = (MAIL_SERVER, MAIL_PORT)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER,
                                  ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')


class CustomJSONEncoder(JSONEncoder):

    def default(self, o):
        from speaklater import is_lazy_string
        if is_lazy_string(o):
            try:
                return unicode(o)
            except NameError:
                return str(o)
        return super(CustomJSONEncoder, self).default(o)


app.json_encoder = CustomJSONEncoder


from app import views, models