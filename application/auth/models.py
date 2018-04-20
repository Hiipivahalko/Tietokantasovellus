from application import db
from application.models import Base

from sqlalchemy.sql import text

# account table scheme
class Account(Base):

  username = db.Column(db.String(144), nullable=False)
  password = db.Column(db.String(144), nullable=False)
  motto = db.Column(db.String(144), nullable=False)
  admin = db.Column(db.Boolean, nullable=False)
  email = db.Column(db.String(144), nullable=False)

  messages = db.relationship("Message", backref='account', lazy=True)
  comments = db.relationship("Comment", backref='account', lazy=True)

  def __init__(self, username, password, motto, email):
    self.username = username
    self.password = password
    self.motto = motto
    self.email = email

  def get_id(self):
    return self.id

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def is_authenticated(self):
    return True


 # query to get single account channels (query result:(id and name))

  @staticmethod
  def find_accounts_channels(account_id):
    stmt = text("SELECT Channel.id, Channel.name FROM Channel, Account, Accounts "
                " WHERE Account.id = :account_id"
                " AND Account.id = Accounts.account_id"
                " AND Accounts.channel_id = Channel.id").params(account_id=account_id)

    res = db.engine.execute(stmt)

    response = []
    for row in res:
      response.append({"id":row[0], "name":row[1]})

    return response
