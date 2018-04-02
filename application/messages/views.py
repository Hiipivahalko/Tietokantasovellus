from flask import render_template, url_for, redirect, request
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm


@app.route("/messages/")
def messages_index():
  return render_template("messages/list.html", messages = Message.query.all())

@app.route("/messages/new/", methods=["GET", "POST"])
@login_required
def messages_create():

  if request.method == "GET":
    return render_template("messages/new.html", form = MessageForm())

  form = MessageForm(request.form)

  if not form.validate():
    return render_template("messages/new.html", form = form)

  message = Message(form.body.data)
  message.account_id = current_user.id

  db.session().add(message)
  db.session().commit()

  return redirect(url_for("messages_index", messages = Message.query.all()))

  
  



