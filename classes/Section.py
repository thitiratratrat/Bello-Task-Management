from mongoengine import *


class Section(Document):
    title = StringField(required=True)
    task_ids = ListField(ObjectIdField(), default=list)
    meta = {
        "collection": "section",
        "ordering": ["-date_created"]
    }

    def addTaskId(self, taskId, taskOrder):
        pushKey = "push__task_ids__{}".format(taskOrder)

        self.update(**{pushKey: [taskId]})

    def editTitle(self, title):
        self.title = title
        
        self.save()

    def removeTaskId(self, taskId):
        self.update(pull__task_ids=taskId)
        
    def reorderTask(self, taskId, taskOrder):
        self.removeTaskId(taskId)
        self.addTaskId(taskId, taskOrder)
