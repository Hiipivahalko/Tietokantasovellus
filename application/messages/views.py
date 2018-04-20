from flask import render_template, url_for, redirect, request
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.channels.models import Channel


# post to write new message to specific channel

@app.route("/messages/new/<channel_id>/", methods=["POST"])
@login_required
def messages_create(channel_id):

  messageform = MessageForm(request.form)

  if not messageform.validate():
    return render_template("messages/new.html", messageform = messageform)

  message = Message(messageform.body.data, current_user.username)
  message.account_id = current_user.id
  message.channel_id = channel_id

  channel = Channel.query.get(channel_id)

  db.session().add(message)
  db.session().commit()

  return redirect(url_for("one_channel_index", channel_id = channel_id, messages = channel.messages))


# Getter to specific message view

@app.route("/channels/<channel_id>/<message_id>/", methods=["GET"])
@login_required
def message_index(channel_id, message_id):

  c = Channel.query.get(channel_id)
  m = Message.query.get(message_id)

  return render_template("messages/message.html", channel = c, message = m, comments = m.comments, messageform=MessageForm())
