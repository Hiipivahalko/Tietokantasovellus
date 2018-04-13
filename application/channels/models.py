from application import db
from application.models import Base
from sqlalchemy.sql import text

# channel and account joint tables 
accounts = db.Table('accounts',
  db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
  db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'), primary_key=True)
)

# channel table scheme
class Channel(Base):

  name = db.Column(db.String(144), nullable=False)
  messages = db.relationship("Message", backref='Channel', lazy=True)

  accounts = db.relationship('Account', secondary=accounts, lazy='subquery',
    backref=db.backref('channels', lazy=True))

  

  def __init__(self, name):
    self.name = name


  @staticmethod
  def find_is_allready_joined(account_id, channel_id):
    stmt = text("SELECT Account.id, Account.username FROM Account, accounts, channel where account.id = accounts.account_id and channel.id = accounts.channel_id and account.id = :account_id and channel.id = :channel_id")

    res = db.engine.execute(stmt)
    totuus = False
    response = []
    for row in res:
      response.append({"id":row[0], "username":row[1]})
      totuus = True
      return totuus
    
    
    return totuus

