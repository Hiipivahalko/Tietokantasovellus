from flask_wtf import FlaskForm
from wtforms import TextField, validators


# form to create new channel or update it

class ChannelForm(FlaskForm):
  name = TextField("Channel name", [validators.Length(min=2)])

  class Meta:
    csrf = False
