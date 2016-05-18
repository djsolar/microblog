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
]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIN_PASSWORD = None

ADMINS = ['you@example.com']

# 每一页显示的博客数量
POSTS_PER_PAGE = 3
# 搜索数据库
WHOOSH_BASE = os.path.join(basedir, 'search.db')
# 搜索结果的数目
MAX_SEARCH_RESULTS = 50
