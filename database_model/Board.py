from mongoengine import *

connect('bello')


class Board(Document):
    _id = ObjectIdField()
    title = StringField(required=True)
    section_ids = ListField(ObjectIdField())
    members = ListField(StringField())

    meta = {
        "collection": "board",
        "ordering": ["-date_created"]
    }
