from application import db
from application.models import Base
from sqlalchemy.sql import text


class Comment(Base):

  body = db.Column(db.Text, nullable=False)
  writer = db.Column(db.String(144), nullable=False)


  # account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
  message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
  account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

  def __init__(self, body, writer):
    self.body = body
    self.writer = writer




