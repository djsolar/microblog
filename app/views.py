#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouyiran'
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'djsolar'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Jim'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for openid = ' + str(form.openid.data) +
              ', remember_me = ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])