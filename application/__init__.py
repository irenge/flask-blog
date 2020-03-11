from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

from application import routes



