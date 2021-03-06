import os

class Config: 
  '''
  General configuration class
  '''
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}' 
  MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
  SECRET_KEY = '2ffb6cc3767911471bc87cd2e8b441ee'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:@localhost/watchlist'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  
  # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
  # simple mde  configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

class ProdConfig(Config): 
  '''
  Production configuration child class
  
  Args: 
      Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql://mbafxodujqpube:ad5b17ac8cba51f36f8db7853f3f50c1280116827eaef5849a03411dd26defd2@ec2-44-198-146-224.compute-1.amazonaws.com:5432/d8vikvlqlr8dis'


class TestConfig(Config): 
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:@localhost/watchlist_test'

class DevConfig(Config): 
  '''
  Development configuration child class
  
  Args: 
      Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:@localhost/watchlist'
  
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production': ProdConfig,
  'test':TestConfig
}