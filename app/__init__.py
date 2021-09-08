from flask import Flask, app
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
  # Initializing application
  app = Flask(__name__)

  # Creating the app configuration
  app.config.from_object(config_options[config_name])

  # Initializing Flask Extensions
  bootstrap.init_app(app)

  # Registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  # Setting config
  from .requests import configure_request
  configure_request(app)
  
  return app