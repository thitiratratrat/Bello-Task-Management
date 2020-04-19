from mongoengine import *


class Section(Document):
    title = StringField(required=True)
    task_ids = ListField(ObjectIdField(), default=list)

    meta = {
        "collection": "section",
        "ordering": ["-date_created"]
    }
