
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.channels.models import Channel
from application.channels.forms import ChannelForm
from application.messages.models import Message
from application.messages.forms import MessageForm


# list of all channels

@app.route("/channels/", methods=["GET"])
@login_required
def channels_index():
  return render_template("channels/list.html", channels = Channel.query.all())



# create new channel

@app.route("/channels/new")
@login_required
def channel_form():
  return render_template("channels/new.html", form = ChannelForm())



# path/method to create new channel if validation is good

@app.route("/channels/", methods=["POST"])
def channels_create():

  form = ChannelForm(request.form)

  if not form.validate():
    return render_template("channels/new.html", form = form)

  channel = Channel(request.form.get("name"))

  channel.accounts.append(current_user)

  db.session().add(channel)
  db.session().commit()

  return redirect(url_for("channels_index"))



# single channel view

@app.route("/channels/<channel_id>/", methods=["GET"])
# @login_required
def one_channel_index(channel_id):
  channel = Channel.query.get(channel_id)
  totuus = False
  id = 0
  if current_user.is_authenticated:
    id = current_user.id

  comments_count = Message.count_how_many_comments()
  print("tän alla")
  print(comments_count)
  print("tulos on täälläääääääääääääää")
  
  return render_template("channels/channel.html", channel = channel,
    form = MessageForm(), messages = channel.messages)



# update channel information

@app.route("/channels/<channel_id>/update/", methods=["GET"])
@login_required
def channel_change(channel_id):

  return render_template("channels/update.html", channel = Channel.query.get(channel_id),
    form = ChannelForm())



# post to update channel

@app.route("/channels/<channel_id>/", methods=["POST"])
@login_required
def channel_update(channel_id):
  c = Channel.query.get(channel_id)
  form = ChannelForm(request.form)

  if not form.validate():
    return render_template("channels/update.html", channel = c, form = form)


  c.name = request.form.get("name")
  db.session().commit()

  return redirect(url_for("channels_index"))



# user join to channel

@app.route("/channel/join/<channel_id>/", methods=["POST"])
@login_required
def channels_join(channel_id):
  channel = Channel.query.get(channel_id)
  account = current_user

  channel.accounts.append(account)
  db.session().commit()

  return redirect(url_for("one_channel_index", channel_id=channel_id))