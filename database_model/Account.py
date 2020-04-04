from mongoengine import *


class Account(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    board_ids = ListField(ObjectIdField(), default=list)

    meta = {'collection': 'account'}
