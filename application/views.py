from flask import render_template, redirect, url_for
from application import app
from application.messages import views
from application.messages.models import Message
from application.channels import views
from application.channels.models import Channel

@app.route("/")
def index():
  channel = Channel.query.get(1)
  return redirect(url_for("one_channel_index", channel_id = 1, messages = channel.messages))