from flask import render_template, redirect, url_for
from application import app
from application.messages import views
from application.messages.models import Message
from application.channels import views
from application.channels.models import Channel
from application.messages.forms import MessageForm
from application.auth.forms import AccountForm, LoginForm
from flask_login import login_required, current_user

@app.route("/")
def index():


    return redirect(url_for('frontpage', sort="first"))

  # return render_template("channels/channel.html", form = MessageForm(), channel = Channel.query.get(channel_id),
    # que = Message.count_how_many_comments(channel_id))


@app.route("/frontpage/<sort>")
def frontpage(sort):

    query = []
    if sort == 'first':
        query=Message.count_how_many_comments_get_first(1)
    elif sort == 'last':
        query = Message.count_how_many_comments_get_last(1)


    channel = Channel.query.get(1)
    account_channels = []
    channels = []
    if current_user.is_authenticated:
        account_channels = Channel.get_my_channels(current_user.id)
        channels = Channel.get_channels_where_not_in(current_user.id)

    return render_template("frontpage.html",
        messageform=MessageForm(),
        accountform=AccountForm(),
        channel=channel,
        que=query,
        loginform=LoginForm(),
        my_channels=account_channels,
        all_channels=channels)
