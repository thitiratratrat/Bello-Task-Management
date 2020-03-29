from mongoengine import *


class Board(Document):
    board_title = StringField(required=True)
    section_title = ListField(StringField())
    members = ListField(StringField())

    meta = {
        "collection": "board",
        "ordering": ["-date_created"]
    }
