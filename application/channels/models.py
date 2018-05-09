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
    introduction = db.Column(db.Text, nullable=False)
    master_id = db.Column(db.Integer, nullable=False)
    messages = db.relationship("Message", backref='Channel', lazy=True)

    accounts = db.relationship('Account', secondary=accounts, lazy='subquery',
        backref=db.backref('channels', lazy=True))



    def __init__(self, name, introduction, master_id):
        self.name = name
        self.introduction = introduction
        self.master_id = master_id


  # query to get channels and how many messages it has

    @staticmethod
    def find_all_channels_and_message_count():
        stmt = text("SELECT Channel.id, Channel.name, count(message.id)"
                        " FROM Channel"
                        " LEFT JOIN Message ON Message.channel_id = Channel.id"
                        " GROUP BY Channel.id")

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


    # check if user is joined to channel

    @staticmethod
    def is_joined(channel_id, account_id):

        stmt = text("SELECT Channel.id"
                    " FROM Channel, Account, Accounts"
                    " WHERE Channel.id = :channel_id"
                    " AND Channel.id = Accounts.channel_id"
                    " AND Account.id = :account_id"
                    " AND Account.id = Accounts.account_id").params(channel_id=channel_id, account_id=account_id)


        res = db.engine.execute(stmt)
        response = False

        for row in res:
            if row[0] == int(channel_id):
                response = True

        return response


    # get channel by name

    @staticmethod
    def get_channel_by_name(channel_name):

        stmt = text("SELECT Channel.id"
                    " FROM Channel"
                    " WHERE Channel.name = :channel_name").params(channel_name=channel_name)

        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

        return null
