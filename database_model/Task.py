from mongoengine import *
from datetime import datetime


class Task(Document):
    title = StringField(required=True)
    responsible_members = ListField(StringField(), default=list)
    due_date = StringField()
    comments = DictField(default={})
    tags = DictField(default={})
    is_finished = BooleanField(default=False)
    meta = {
        "collection": "task",
        "ordering": ["-date_created"]
    }

    def getTitle(self):
        return self.title

    def getResponsibleMembers(self):
        return self.responsible_members

    def getDueDate(self):
        return self.due_date

    def getComments(self):
        return self.comments

    def getTags(self):
        return self.tags

    def getIsFinished(self):
        return self.is_finished

    def addTag(self, tag, color):
        self.tags[tag] = color

        self.save()

    def addComment(self, comment, memberUsername):
        self.comments[comment] = memberUsername
        self.save()

    def addResponsibleMemberUsername(self, memberUsername):
        self.responsible_members.append(memberUsername)
        self.save()

    def setDueDate(self, dueDate):
        self.due_date = dueDate

        self.save()

    def editTitle(self, title):
        self.title = title

        self.save()

    def setTaskFinishState(self, state):
        self.is_finished = state

        self.save()
