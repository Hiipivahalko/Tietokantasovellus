from application import db
from application.models import Base
from sqlalchemy.sql import text


# Comment table schema

class Comment(Base):

    body = db.Column(db.Text, nullable=False)
    writer = db.Column(db.String(144), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, body, writer):
        self.body = body
        self.writer = writer


    @staticmethod
    def get_comment_message_and_channel_id(account_id):

        stmt = text("SELECT Comment.id, Comment.body, Comment.message_id, Message.channel_id"
                    " FROM Comment, Message"
                    " WHERE Comment.message_id = Message.id"
                    " AND Comment.account_id = :account_id").params(account_id=account_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"comment_id":row[0], "comment_body":row[1], "message_id":row[2], "channel_id":row[3]})

        return response
