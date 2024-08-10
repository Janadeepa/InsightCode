import os

class Config:
    # Configuration settings for the application
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    DEBUG = os.environ.get('DEBUG') or True
    # Add other configuration variables here as needed
