from application import app, db
from flask import render_template, request, url_for, redirect
from application.sports.models import Sport

@app.route("/sports/", methods=["GET"])
def sports_index():
  return render_template("sports/list.html", sports = Sport.query.all())

@app.route("/sports/new")
def sports_form():
  return render_template("sports/new.html")

@app.route("/sports/", methods=["POST"])
def sports_create():

  sport = Sport(request.form.get("name"))

  db.session().add(sport)
  db.session().commit()

  return redirect(url_for("sports_index"))

@app.route("/sports/<sport_id>/", methods=["GET"])
def one_sport_index(sport_id):
  return render_template("sports/sport.html", sport = Sport.query.get(sport_id))


@app.route("/sports/<sport_id>/update/", methods=["GET"])
def sport_change(sport_id):

  return render_template("sports/update.html", sport = Sport.query.get(sport_id))

@app.route("/sports/<sport_id>/", methods=["POST"])
def sport_update(sport_id):
  s = Sport.query.get(sport_id)
  s.name = request.form.get("newName")
  db.session().commit()

  return redirect(url_for("sports_index"))