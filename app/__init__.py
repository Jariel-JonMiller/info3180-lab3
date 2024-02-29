from flask import Flask
from flask_mail import Mail 
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

'''app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '88c87371b0d780'
app.config['MAIL_PASSWORD'] = '********7f03'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False'''
 
mail = Mail(app)
from app import views