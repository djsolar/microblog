#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouyiran'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "a hard string"

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
    {'name': 'QQ', 'url': 'https://graph.z.qq.com/moc2/me'}
]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIN_PASSWORD = os.environ.get('MAIL_PASSWORD')

ADMINS = ['djsolar1999@gmail.com']

# 每一页显示的博客数量
POSTS_PER_PAGE = 3
# 搜索数据库
WHOOSH_BASE = os.path.join(basedir, 'search.db')
# 搜索结果的数目
MAX_SEARCH_RESULTS = 50

LANGUAGES = {
    'es': 'English',
    'es': 'Español'
}

MS_TRANSLATOR_CLIENT_ID = ''
MS_TRANSLATOR_CLIENT_SECRET = ''
