from application.comments.models import Comment


from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.channels.models import Channel
from application.channels.forms import ChannelForm
from application.messages.models import Message
from application.messages.forms import MessageForm


@app.route("/channel/<channel_id>/message/<message_id>/newcomment/", methods=["POST"])
def message_new_comment(channel_id, message_id):

  form = MessageForm(request.form)

  if not form.validate():
    return redirect(url_for("message_index", channel_id=channel_id, message_id=message_id))

  comment = Comment(form.body.data, current_user.username)
  comment.message_id = message_id
  comment.account_id = current_user.id

  db.session().add(comment)
  db.session().commit()

  return redirect(url_for("message_index", channel_id=channel_id, message_id=message_id))