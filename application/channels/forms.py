from flask_wtf import FlaskForm
from wtforms import TextField, validators, TextAreaField


# form to create new channel or update it

class ChannelForm(FlaskForm):
    name = TextField("Channel name", [validators.Length(min=2), validators.DataRequired()])
    introduction = TextAreaField("Introduction", [validators.Length(min=2), validators.DataRequired()])

    class Meta:
        csrf = False
