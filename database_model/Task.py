from mongoengine import *
from datetime import datetime


class Task(Document):
    title = StringField(required=True)
    responsible_members = ListField(StringField(), default=list)
    due_date = DateTimeField()
    comments = ListField(StringField(), default=list)
    tags = ListField(StringField(), default=list)

    meta = {
        "collection": "task",
        "ordering": ["-date_created"]
    }
