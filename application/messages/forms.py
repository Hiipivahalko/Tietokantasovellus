from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


# Form to create new message or comment

class MessageForm(FlaskForm):
    body = TextAreaField("Write your message: ", [validators.Length(min=2)])

    class Meta:
        csrf = False
