from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField, validators, SelectField

# form to login
class LoginForm(FlaskForm):
  username = TextField("Username", [validators.Length(min=2), validators.DataRequired()])
  password = PasswordField("Password", [validators.Length(min=2), validators.DataRequired()])

  class Meta:
    csrf = False


# form to create new account

class AccountForm(FlaskForm):
  username = TextField("Username", [validators.Length(min=2), validators.DataRequired()])
  password = PasswordField("Password", [validators.Length(min=8), validators.DataRequired()])
  password2 = PasswordField("Password Again", [validators.Length(min=8), validators.DataRequired()])
  motto = TextField("Motto", [validators.Length(min=2), validators.DataRequired()])
  email = TextField("Email", [validators.Length(min=2), validators.DataRequired(), validators.Email()])


  class Meta:
    csrf = False
