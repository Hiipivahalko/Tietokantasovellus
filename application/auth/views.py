from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db

from application.auth.models import Account
from application.auth.forms import LoginForm, AccountForm
from application.channels.models import Channel
from application.channels import models
from application.messages.models import Message
from application.messages import views
from application.comments.models import Comment

# login to account

@app.route("/auth/login/", methods=["GET", "POST"])
def auth_login():

  if request.method == "GET":
    return render_template("auth/loginform.html", loginform = LoginForm(),
        my_channels=Channel.get_my_channels(-1),
        all_channels=[])

  loginform = LoginForm(request.form)
  account = Account.query.filter_by(username=loginform.username.data,
    password=loginform.password.data).first()

  if not account:
    return render_template("auth/loginform.html", loginform = loginform,
      error = "No such username or password")

  print("käyttäjä " + account.username + " tunnistettiin, JEEE :)")
  login_user(account)

  return redirect(url_for("one_channel_index", channel_id=1, sort='first'))



# logout

@app.route("/auth/logout")
def auth_logout():
  logout_user()
  return redirect(url_for("index"))


# account view

@app.route("/account/", methods=["GET"])
@login_required
def single_account_index():
  return render_template("auth/index.html", account = current_user, accountform = AccountForm(),
    channels = Account.find_accounts_channels(current_user.id),
    my_channels=Channel.get_my_channels(current_user.id),
    all_channels=Channel.get_channels_where_not_in(current_user.id))


# create new account

@app.route("/auth/new/", methods=["GET", "POST"])
def account_create():

    if request.method == "GET":
        return render_template("auth/new.html",
        accountform = AccountForm(),
        my_channels=Channel.get_my_channels(-1),
        all_channels=[])

    accountform = AccountForm(request.form)

    not_same = False

    if not accountform.password.data == accountform.password2.data:
        not_same = True

    if not accountform.validate() or not_same == True:
        return render_template("frontpage.html",
                                accountform = AccountForm())

    account = Account(accountform.username.data, accountform.password.data, accountform.motto.data, accountform.email.data)

    if current_user.is_authenticated:
        if request.form.get("super") == "True":
            account.admin = True
    else:
        account.admin = False

    channel = Channel.query.get(1)

    channel.accounts.append(account)

    db.session().add(account)
    db.session().commit()

    # this happens if admin is creating account
    if current_user.is_authenticated:
        redirect(url_for('one_channel_index', channel_id=1, sort='first'))

    return redirect(url_for("auth_login"))


# update account

@app.route("/auth/update/<account_id>/", methods=["POST"])
def accounts_update(account_id):

    accountform = AccountForm(request.form)

    # check if username is whitespaces only

    char1 = False
    email = False
    not_same = False

    messages = []
    messages.append("*username must be 2 character length")
    messages.append("*password must be 8 character length")
    messages.append("*motto must be 2 character length")
    messages.append("*email must be 6 character length and must be real email")

    # email check
    for c in accountform.email.data:
        if c == '@':
            char1 = True

        if char1 == True:
            if c == '.':
                email = True

    if not accountform.password.data == accountform.password2.data:
        messages.append("*password was not same")
        not_same = True

    if not accountform.validate() or email == False or accountform.username.data.isspace() or not_same == True:
        return render_template("auth/index.html",
                                accountform = AccountForm(),
                                errors = messages,
                                account=current_user,
                                my_channels=Channel.get_my_channels(current_user.id),
                                all_channels=Channel.get_channels_where_not_in(current_user.id),
                                channels=Account.find_accounts_channels(current_user.id))

    account = Account.query.get(account_id)

    account.username = accountform.username.data
    account.password = accountform.password.data
    account.motto = accountform.motto.data
    account.email = accountform.email.data

    db.session().commit()

    return redirect(url_for("single_account_index"))


# list all account to admin user

@app.route("/auth/allAccount/", methods=["GET"])
@login_required
def account_list():

    if current_user.admin == False:
        return redirect(url_for("messages_index"))

    if request.method == "GET":
        return render_template("auth/list.html",
                                accounts = Account.query.order_by(Account.username).all(),
                                my_channels=Channel.get_my_channels(current_user.id),
                                all_channels=Channel.get_channels_where_not_in(current_user.id))


# delete account (admin user can only do that), deleting also account messages (and messages all comments),comments

@app.route("/auth/delete/<account_id>/", methods=["POST"])
def accounts_delete(account_id):
    account = Account.query.get(account_id)
    messages = Message.query.filter_by(account_id=account_id).all()

    for message in messages:
        Comment.query.filter_by(message_id=message.id).delete()
        db.session().delete(message)

    Comment.query.filter_by(account_id=account_id).delete()

    db.session().delete(account)
    db.session().commit()

    return redirect(url_for("account_list"))
