#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouyiran'
from app import db


# 用户表
class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)


# 用户发表的文章
class Post(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' %(self.body)