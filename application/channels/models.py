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



  # query to get channels and how many messages it has

  @staticmethod
  def find_all_channels_and_message_count():
      stmt = text("SELECT Channel.id, Channel.name, count(message.id)"
                        " FROM Channel"
                        " left join Message on message.channel_id = channel.id"
                        " group by channel.id")

      res = db.engine.execute(stmt)

      response = []
      for row in res:
        response.append({"id":row[0],"name":row[1], "message_count":row[2]})

      return response


  # query to get channels were account has joined

  @staticmethod
  def get_my_channels(account_id):

    stmt = text("SELECT Channel.id, Channel.name"
                    " FROM Channel, Account, Accounts"
                    " WHERE Channel.id = Accounts.channel_id"
                    " AND Account.id = Accounts.account_id"
                    " AND Account.id = :account_id").params(account_id=account_id)

    res = db.engine.execute(stmt)

    response = []

    for row in res:
        response.append({"channel_id":row[0], "channel_name":row[1]})

    
    return response


  # query to get all other channels that account not joined

  @staticmethod
  def get_channels_where_not_in(account_id):

      stmt = text("SELECT channel.id, channel.name"
                    " FROM Channel"
                    " WHERE Channel.id NOT IN ("
                        " SELECT Channel.id"
                            " FROM Channel, Account, Accounts"
                            " WHERE Channel.id = Accounts.channel_id"
                            " AND Account.id = Accounts.account_id"
                            " AND Account.id = :account_id"
                    " )").params(account_id=account_id)

      res = db.engine.execute(stmt)

      response = []

      for row in res:
          response.append({"id":row[0], "name":row[1]})

      return response
