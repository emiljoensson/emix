#! /usr/bin/env python3
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True