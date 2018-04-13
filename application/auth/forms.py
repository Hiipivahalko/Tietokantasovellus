from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField, validators

# form to login
class LoginForm(FlaskForm):
  username = TextField("Username: ", [validators.length(min=2)]) 
  password = PasswordField("Password: ", [validators.length(min=8)]) 

  class Meta:
    csrf = False

class AccountForm(FlaskForm):
  username = TextField("Username: ", [validators.length(min=2)]) 
  password = PasswordField("Password: ", [validators.length(min=8)])
  motto = TextField("Motto: ", [validators.length(min=2)])
  email = TextField("Email: ", [validators.length(min=2)])

  class Meta:
    csrf = False