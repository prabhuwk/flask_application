#!/usr/bin/env python
from myapp import create_app, db
from myapp.models import User

if __name__ == '__main__':
	app = create_app('development')
	with app.app_context():
		db.create_all()
	app.run()
