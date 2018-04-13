from application import db
from application.models import Base

from sqlalchemy.sql import text

class Message(Base):

  body = db.Column(db.Text, nullable=False)
  writer = db.Column(db.String(144), nullable=False)

  account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
  channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)

  #  messages = db.relationship("Message", backref='account', lazy=True)
  comments = db.relationship("Comment", backref='message', lazy=True)

  def __init__(self, body, writer):
    self.body = body
    self.writer = writer

  @staticmethod
  def count_how_many_comments():
    stmt = text("SELECT count(*) from Comment, Message"
                " WHERE message.id = 1 and"
                " message.id = comment.message_id")

    res = db.engine.execute(stmt)
    # result = res[0]
    print(res)
    return res




