
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db, views
from application.channels.models import Channel
from application.channels.forms import ChannelForm
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.comments.models import Comment



# create new channel

@app.route("/channels/new")
@login_required
def channel_form():
    return render_template("channels/new.html", channelform = ChannelForm(), my_channels=Channel.get_my_channels(current_user.id),
        all_channels=Channel.get_channels_where_not_in(current_user.id))



# create new channel if validation is good

@app.route("/channels/", methods=["POST"])
@login_required
def channels_create():

    channelform = ChannelForm(request.form)

    if not channelform.validate():
        return render_template("channels/new.html", channelform = channelform,
            my_channels=Channel.get_my_channels(current_user.id),
            all_channels=Channel.get_channels_where_not_in(current_user.id))

    channel = Channel(channelform.name.data, channelform.introduction.data, current_user.id)

    channel.accounts.append(current_user)

    db.session().add(channel)
    db.session().commit()

    new_channel = Channel.get_channel_by_name(channel.name)

    return redirect(url_for("one_channel_index", channel_id=new_channel, sort='first'))



# single channel view

@app.route("/channels/<channel_id>/<sort>/", methods=["GET"])
@login_required
def one_channel_index(channel_id, sort):

    if channel_id == "1":
        return redirect(url_for('frontpage', sort="first"))

    query = []

    if sort == 'first':
        query= Message.count_how_many_comments_get_first(channel_id)
    elif sort == 'last':
        query = Message.count_how_many_comments_get_last(channel_id)

    return render_template("channels/channel.html",
                            messageform = MessageForm(),
                            channel = Channel.query.get(channel_id),
                            que = query ,
                            my_channels=Channel.get_my_channels(current_user.id),
                            all_channels=Channel.get_channels_where_not_in(current_user.id),
                            allready_join = Channel.is_joined(channel_id, current_user.id))



# update channel information

@app.route("/channels/<channel_id>/update/", methods=["GET"])
@login_required
def channel_change(channel_id):

    return render_template("channels/update.html", channel = Channel.query.get(channel_id),
        channelform = ChannelForm(), my_channels=Channel.get_my_channels(current_user.id),
        all_channels=Channel.get_channels_where_not_in(current_user.id))



# update channel

@app.route("/channels/<channel_id>/", methods=["POST"])
@login_required
def channel_update(channel_id):
    c = Channel.query.get(channel_id)
    channelform = ChannelForm(request.form)

    if not channelform.validate():
        return render_template("channels/update.html", channel = c, channelform = channelform,
            my_channels=Channel.get_my_channels(current_user.id),
            all_channels=Channel.get_channels_where_not_in(current_user.id))

    c.name = channelform.name.data
    c.introduction = channelform.introduction.data
    db.session().commit()

    return redirect(url_for("one_channel_index", channel_id=channel_id, sort='first'))



# join to channel


@app.route("/channel/join/<channel_id>/", methods=["POST"])
@login_required
def channels_join(channel_id):
    channel = Channel.query.get(channel_id)
    account = current_user

    channel.accounts.append(account)
    db.session().commit()

    return redirect(url_for("one_channel_index", channel_id=channel_id, sort='first'))



# Channels manager

@app.route("/channel/manage/", methods=["GET"])
@login_required
def channel_manager():

    return render_template("channels/manager.html", channels = Channel.query.all(),
        my_channels=Channel.get_my_channels(current_user.id),
        all_channels=Channel.get_channels_where_not_in(current_user.id))


# DELETE Channel

@app.route("/channel/<channel_id>/delete/", methods=["POST"])
@login_required
def delete_channel(channel_id):
    channel = Channel.query.get(channel_id)
    messages = Message.query.filter_by(channel_id=channel_id).all()

    for message in messages:
        Comment.query.filter_by(message_id=message.id).delete()
        db.session().delete(message)

    db.session().delete(channel)
    db.session().commit()

    return redirect(url_for("channel_manager"))
