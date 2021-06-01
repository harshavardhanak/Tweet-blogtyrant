from enum import unique
from flask import Flask
from flask.scaffold import F
from flask.templating import render_template
import sqlalchemy
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8bd20d7393e2157407c0cb2538286beb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://emfbrddvyyjwrb:a59c96479e251f4993d773d0c2bcf163d221d2934ac00138e3f17d6a635412ef@ec2-54-91-188-254.compute-1.amazonaws.com:5432/dbkd3reijfh1b6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'harshavardhanakhv@gmail.com'
app.config['MAIL_PASSWORD'] = '9741722649'
#cprops.put("mail.smtp.starttls.enable", "true")
mail = Mail(app)

from flaskblog import routes
