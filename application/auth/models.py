from application import db

# account table scheme
class Account(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
  
  username = db.Column(db.String(144), nullable=False)
  password = db.Column(db.String(144), nullable=False)
  motto = db.Column(db.String(144), nullable=False)
  admin = db.Column(db.Boolean, nullable=False)

  messages = db.relationship("Message", backref='account', lazy=True)

  def __init__(self, username, password, motto):
    self.username = username
    self.password = password
    self.motto = motto

  def get_id(self):
    return self.id

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def is_authenticated(self):
    return True