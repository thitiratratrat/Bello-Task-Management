from mongoengine import *


class Account(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    board_id = ListField(IntField(), default=list)

    meta = {'collection': 'account'}
