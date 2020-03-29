from mongoengine import *


class Account(Document):
    username = StringField(required=True)
    password = StringField(required=True)

    meta = {'collection': 'account'}
