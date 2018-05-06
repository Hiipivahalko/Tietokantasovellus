from flask import render_template, url_for, redirect, request
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.channels.models import Channel
from application.comments.models import Comment


# write new message to specific channel

@app.route("/messages/new/<channel_id>/", methods=["POST"])
@login_required
def messages_create(channel_id):

    messageform = MessageForm(request.form)
    channel = Channel.query.get(channel_id)

    if not messageform.validate():
        return render_template("channels/channel.html", messageform = MessageForm(), channel = channel,
            que = Message.count_how_many_comments(channel_id), my_channels=Channel.get_my_channels(current_user.id),
            all_channels=Channel.get_channels_where_not_in(current_user.id), allready_join = Channel.is_joined(channel_id, current_user.id),
            error="message must be 2 character length")


    message = Message(messageform.body.data, current_user.username)
    message.account_id = current_user.id
    message.channel_id = channel_id

    db.session().add(message)
    db.session().commit()

    return redirect(url_for("one_channel_index", channel_id = channel_id, sort='first'))


# message view

@app.route("/channels/message/<channel_id>/<message_id>/", methods=["GET"])
@login_required
def message_index(channel_id, message_id):

    c = Channel.query.get(channel_id)
    m = Message.query.get(message_id)

    comments = []

    if m is not None:
        comments = m.comments

    return render_template("messages/message.html", channel = c, message = m, comments = comments, messageform=MessageForm(),
        all_channels = Channel.get_channels_where_not_in(current_user.id), my_channels = Channel.get_my_channels(current_user.id))

# DELETE MESSAGE

@app.route("/channels/<channel_id>/<message_id>/delete/", methods=["POST"])
@login_required
def delete_message(channel_id, message_id):

    message = Message.query.get(message_id)
    Comment.query.filter_by(message_id=message_id).delete()

    db.session().delete(message)
    db.session().commit()

    return redirect(url_for("one_channel_index", channel_id=channel_id, sort='first'))
