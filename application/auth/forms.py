from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField, validators

# form to login
class LoginForm(FlaskForm):
  username = TextField("Username", [validators.Length(min=2)])
  password = PasswordField("Password", [validators.Length(min=2)])

  class Meta:
    csrf = False


# form to create new account

class AccountForm(FlaskForm):
  username = TextField("Username", [validators.Length(min=2)])
  password = PasswordField("Password", [validators.Length(min=8)])
  password2 = PasswordField("Password Again", [validators.Length(min=8)])
  motto = TextField("Motto", [validators.Length(min=2)])
  email = TextField("Email", [validators.Length(min=2)])

  class Meta:
    csrf = False
