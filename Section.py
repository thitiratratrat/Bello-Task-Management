from mongoengine import *


connect('Section',  host = "localhost", port=27017)

class Section(Document):
    
    _id = ObjectIdField()
    tasks=ListField(StringField(), default=list)
    
    
    meta= {
        "collection": "section",
        "ordering":["-date_created"]
    }
s=Section(
    tasks=["mongoengine"]

).save()

