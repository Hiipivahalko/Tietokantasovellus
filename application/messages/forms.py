from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class MessageForm(FlaskForm):
  body = TextAreaField("Write your message: ", [validators.length(min=2)])

  class Meta:
    csrf = False