import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
WTF_CSRF_SECRET_KEY = 'a random string'


from app import views, models