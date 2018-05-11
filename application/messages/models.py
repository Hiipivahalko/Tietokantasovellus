from application import db
from application.models import Base

from sqlalchemy.sql import text

class Message(Base):

    body = db.Column(db.Text, nullable=False)
    writer = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)

    comments = db.relationship("Comment", backref='message', lazy=True)

    def __init__(self, body, writer):
        self.body = body
        self.writer = writer


    # query to get messages comments count

    @staticmethod
    def count_how_many_comments_get_first(channel_id):
        stmt = text("SELECT Channel.id, Message.id, Channel.name, Message.body, COUNT(Comment.id), Message.writer, Message.date_created, Message.account_id, Account.motto"
                    " FROM Channel, Message, Account"
                    " LEFT JOIN Comment ON Message.id = Comment.message_id"
                    " WHERE Channel.id = Message.channel_id"
                    " and Channel.id = :channel_id"
                    " AND Account.id = Message.account_id"
                    " GROUP BY Channel.id, Message.id"
                    " ORDER BY Message.date_created DESC").params(channel_id=channel_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"channel_id":row[0],
                            "message_id":row[1],
                            "channel_name":row[2],
                            "body":row[3],
                            "comment_count":row[4],
                            "writer":row[5],
                            "date":row[6],
                            "account_id":row[7],
                            "motto":row[8] })


        return response

    @staticmethod
    def count_how_many_comments_get_last(channel_id):
        stmt = text("SELECT Channel.id, Message.id, Channel.name, Message.body, COUNT(Comment.id), Message.writer, Message.date_created, Message.account_id, Account.motto"
                    " FROM Channel, Message, Account"
                    " LEFT JOIN Comment ON Message.id = Comment.message_id"
                    " WHERE Channel.id = Message.channel_id"
                    " and Channel.id = :channel_id"
                    " AND Account.id = Message.account_id"
                    " GROUP BY Channel.id, Message.id"
                    " ORDER BY Message.date_created ASC").params(channel_id=channel_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"channel_id":row[0],
                            "message_id":row[1],
                            "channel_name":row[2],
                            "body":row[3],
                            "comment_count":row[4],
                            "writer":row[5],
                            "date":row[6],
                            "account_id":row[7],
                            "motto":row[8] })


        return response
