from mongoengine import *


class Task(Document):
    title = StringField(required=True)
    responsible_member = StringField()
    due_date = StringField()
    comments = ListField(DictField(default={}), default=list)
    tags = DictField(default={})
    is_finished = BooleanField(default=False)
    meta = {
        "collection": "task",
        "ordering": ["-date_created"]
    }

    def addTag(self, tag, color):
        self.tags[tag] = color

        self.save()

    def addComment(self, comment, memberUsername, commentOrder):
        pushKey = "push__comments__{}".format(commentOrder)
        
        self.update(**{pushKey: [{memberUsername: comment}]})

    def setTaskResponsibleMember(self, memberUsername):
        self.responsible_member = memberUsername
        
        self.save()

    def setDueDate(self, dueDate):
        self.due_date = dueDate

        self.save()

    def setFinishState(self, state):
        self.is_finished = state

        self.save()

    def editTitle(self, title):
        self.title = title

        self.save()
        
    def removeComment(self, commentOrder):
        unsetKey = "unset__comments__{}".format(commentOrder)
        
        self.update(**{unsetKey: [1]})
        self.update(pull__comments=None)
        
    def removeTag(self, tag):
        unsetKey = "unset__tags__{}".format(tag)
        
        self.update(**{unsetKey: [1]})
        
        