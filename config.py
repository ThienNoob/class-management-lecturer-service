import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://{}:27017'.format(os.getenv('HOST_NAME')))