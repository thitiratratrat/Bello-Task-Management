from mongoengine import *
from datetime import datetime
connect('Task',  host = "localhost", port=27017)

class Task(Document):
    _id = ObjectIdField()
    title = StringField(required=True)
    responsiblemembers = ListField(StringField(), default=list)
    dueDate=DateTimeField()
    comment=ListField(StringField(), default=list)
    tags=ListField(StringField(), default=list)


    meta = {
        "collection": "task",
        "ordering": ["-date_created"]
    }


t=Task(
    title="work",
    responsiblemembers=["chanyanuch","oranich"] ,   
    dueDate=("2016-05-18"),
    comment=["hahaha","suuuu"],
    tags=["blue","pink"]


).save()