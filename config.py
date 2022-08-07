import os

# creating a configuration class
class Config(object):
    # Local config
    SECRET_KEY = "{ENTER YOUR SECRET KEY}"
    MONGO_URI =  "{YOUR MONGODB CONNECTION STRING}"
    BASE_URL = "http://127.0.0.1:5000"

    # If Heroku hosting, comment out parameters above; uncomment and set values for the parameters below
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # MONGO_URI =  os.environ.get('MONGO_URI')
    # BASE_URL = os.environ.get('BASE_URL')

