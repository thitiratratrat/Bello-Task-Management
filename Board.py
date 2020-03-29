from mongoengine import *


class Board(Document):
    boardId=IntField(unique=True)
    boardTitle=StringField(required=True)
    sectionTitle=ListField(StringField())
    members=ListField(StringField())
    
    
    meta= {
        "collection": "board",
        "ordering":["-date_created"]
    }

