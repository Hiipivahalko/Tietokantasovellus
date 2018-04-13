from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import Account
from application.auth.forms import LoginForm, AccountForm
from application.channels import models
from application.messages.models import Message
from application.messages import views

# login to account

@app.route("/auth/login/", methods=["GET", "POST"])
def auth_login():
  
  if request.method == "GET":
    return render_template("auth/loginform.html", form = LoginForm())

  form = LoginForm(request.form)
  account = Account.query.filter_by(username=form.username.data, 
    password=form.password.data).first()

  if not account:
    return render_template("auth/loginform.html", form = form,
      error = "No such username or password")

  print("käyttäjä " + account.username + " tunnistettiin, JEEE :)")
  login_user(account)

  return redirect(url_for("one_channel_index", channel_id = 1, messages = Message.query.all()))



# logout

@app.route("/auth/logout")
def auth_logout():
  logout_user()
  return redirect(url_for("index"))



# account view

@app.route("/account/", methods=["GET"])
@login_required
def single_account_index():
  return render_template("auth/index.html", account = current_user, form = AccountForm(),
    channels = Account.find_accounts_channels(current_user.id))




# create new account

@app.route("/auth/new/", methods=["GET", "POST"])
def account_create():
  if request.method == "GET":
    return render_template("auth/new.html", form = AccountForm())

  form = AccountForm(request.form)

  if not form.validate():
    messages = []
    messages.append("*username must be 2 character length") 
    messages.append("*password must be 8 character length")
    messages.append("*username must be 2 character length")    
    return render_template("auth/new.html", form = AccountForm(),
      errors = messages)

  account = Account(form.username.data, form.password.data, form.motto.data, form.email.data)
  account.admin = False

  db.session().add(account)
  db.session().commit()

  return redirect(url_for("one_channel_index", channel_id = 1, messages = Message.query.all()))




# update account

@app.route("/auth/update/<account_id>/", methods=["POST"])
def accounts_update(account_id):
  
  form = AccountForm(request.form)

  if not form.validate():
    messages = []
    messages.append("*username must be 2 character length") 
    messages.append("*password must be 8 character length")
    messages.append("*username must be 2 character length")    
    return render_template("auth/index.html", form = AccountForm(),
      errors = messages, account=current_user)

  account = Account.query.get(account_id)

  account.username = form.username.data
  account.password = form.password.data
  account.motto = form.motto.data
  account.email = form.email.data

  db.session().commit()

  return redirect(url_for("single_account_index"))




# list all account to admin user

@app.route("/auth/allAccount/", methods=["GET"])
@login_required
def account_list():

  if current_user.admin == False:
    return redirect(url_for("messages_index"))

  if request.method == "GET":
    return render_template("auth/list.html", accounts = Account.query.all())





# delete account (admin user can only do that)

@app.route("/auth/delete/<account_id>/", methods=["POST"])
def accounts_delete(account_id):
  account = Account.query.get(account_id)
  Message.query.filter_by(account_id=account_id).delete()

  db.session().delete(account)
  db.session().commit()

  return redirect(url_for("account_list"))




 
