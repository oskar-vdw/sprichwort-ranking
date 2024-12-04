import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy modification tracking
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Store your secret key in env variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://oskarpsql:34xuK%233-21.d@localhost:5432/devsr'