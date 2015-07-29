from . import main
from flask import render_template, redirect, url_for, request
from flask.ext.login import login_required, login_user, logout_user, current_user
from .forms import LoginForm
from ..models import User
import ldap

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data

		try: 
			User.try_login(username,password)
		except ldap.INVALID_CREDENTIALS:
			return redirect(url_for('main.login', **request.args))
		
		user = User.query.filter_by(username=form.username.data).first()
		if not user:
			User.register(username,password)
		login_user(user, form.remember_me.data)
		return redirect(request.args.get('next') or url_for('main.index'))
	return render_template('login.html', form=form)
