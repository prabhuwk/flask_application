import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
	#Create application instance
	app = Flask(__name__)
	
	#import configuration
	cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
	app.config.from_pyfile(cfg)
	
	#initialize extensions
	bootstrap.init_app(app)

	#import blueprints
	from .main import main as main_blueprint 
	app.register_blueprint(main_blueprint)

	return app
