from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forum.db"
  app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# application functionality
from application import views

from application.channels import models
from application.channels import views

from application.auth import models
from application.auth import views

from application.messages import models
from application.messages import views

from application.comments import models
from application.comments import views

# login
from application.auth.models import Account
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(account_id):
  return Account.query.get(account_id)


# create tables to database if necessary
try:
  db.create_all()
except:
  pass
