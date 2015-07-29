from werkzeug.security import generate_password_hash, check_password_hash
from . import db, lm
from flask.ext.login import UserMixin
import ldap

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(16), index=True, unique=True)
	password_hash = db.Column(db.String(64))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	@staticmethod
	def try_login(username, password):
		conn = ldap.initialize('ldap://ldap.example.com')
		conn.protocol_version = ldap.VERSION3
		conn.simple_bind_s('uid=%s,ou=people,dc=example,dc=com' %username,password)
		print "connected by ", username
	
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return unicode(self.id)

	@staticmethod
	def register(username, password):
		user = User(username=username)
		user.set_password(password)
		db.session.add(user)
		db.session.commit()

	def __repr__(self):
		return '<User {0}>'.format(self.username)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
