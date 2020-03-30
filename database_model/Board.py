from mongoengine import *

connect('bello')


class Board(Document):
    _id = ObjectIdField()
    title = StringField(required=True)
    section_ids = ListField(ObjectIdField(), default=list)
    members = ListField(StringField(), default=list)

    meta = {
        "collection": "board",
        "ordering": ["-date_created"]
    }