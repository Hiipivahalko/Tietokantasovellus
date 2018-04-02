from flask import render_template, redirect, url_for
from application import app
from application.messages import views

@app.route("/")
def index():
  return redirect(url_for("messages_index"))