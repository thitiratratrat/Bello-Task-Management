from mongoengine import *


class Section(Document):
    _id = ObjectIdField()
    title = StringField(required=True)
    task_ids = ListField(StringField(), default=list)

    meta = {
        "collection": "section",
        "ordering": ["-date_created"]
    }
