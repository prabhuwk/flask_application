from . import main
from flask import render_template, redirect, url_for, request
from flask.ext.login import login_required, login_user, logout_user, current_user
from .forms import LoginForm

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
