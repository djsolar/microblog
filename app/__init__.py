#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouyiran'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
from app import views, models
