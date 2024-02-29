import os
from dotenv import load_dotenv

load_dotenv()

class Config(object): 
    """Base Config Object""" 
    DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y') 
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '2525') 
    MAIL_USERNAME = os.environ.get('88c87371b0d780') 
    MAIL_PASSWORD = os.environ.get('27dcbd52b47f03')
