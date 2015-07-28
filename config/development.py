import os
DEBUG = True
SECRET_KEY = 'some secret key!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
	os.path.dirname(__file__), '../development.sqlite3')
