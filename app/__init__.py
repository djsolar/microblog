#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouyiran'
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
