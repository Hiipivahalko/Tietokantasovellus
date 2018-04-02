from application import db

# channel and account joint tables 
accounts = db.Table('accounts',
  db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
  db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'), primary_key=True)
)

# channel table scheme
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

