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

@app.route("/frontpage/<sort>/")
def frontpage(sort):

    if current_user.is_authenticated:
        return redirect(url_for('one_channel_index', channel_id=1, sort='first'))

    return render_template("frontpage.html",
        accountform=AccountForm())
