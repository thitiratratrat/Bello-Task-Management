from mongoengine import *


class Board(Document):
    title = StringField(required=True)
    section_ids = ListField(ObjectIdField(), default=list)
    members = ListField(StringField(), default=list)

    meta = {
        "collection": "board",
        "ordering": ["-date_created"]
    }
