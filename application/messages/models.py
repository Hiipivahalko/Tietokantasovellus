from application import db

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

  body = db.Column(db.Text, nullable=False)

  account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

  def __init__(self, body):
    self.body = body

"""
class Channel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

  name = db.Column(db.String(144), nullable=False)

  accounts = db.relationship('Account', secondary=accounts, lazy='subquery',
    backref=db.backref('channels', lazy=True))

  def __init__(self, name):
    self.name = name
"""

