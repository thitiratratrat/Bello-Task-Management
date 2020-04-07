from mongoengine import *

connect('Board',  host = "localhost", port=27017)

class Board(Document):
    _id = ObjectIdField()
    title = StringField(required=True)
    section_ids = ListField(ObjectIdField(), default=list)
    members = ListField(StringField(), default=list)

    meta = {
        "collection": "board",
        "ordering": ["-date_created"]
    }


b=Board(
    title="work",
    section_ids = ["507f191e810c19729de860ea","507f1f77bcf86cd799439011"],
    members=["chanyanuch","oranich"]    

).save()