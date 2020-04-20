from typing import List


class Section:
    def __init__(self, title, id, tasks={}):
        self.__id = id
        self.__title = title
        self.__tasks = tasks
        self.__taskOrders = []
    
    def getId(self):
        return self.__id

    def getTitle(self) -> str:
        return self.__title

    def getTasks(self):
        return self.__tasks

    def editTitle(self, title):
        self.__title = title

    def addTask(self, taskOrder, task):
        self.__tasks[task.getId()] = task
        
        self.__taskOrders.insert(taskOrder, task.getId())
        
    def addTaskComment(self, taskId, taskComment):
        task = self.__tasks[taskId]
        
        task.addComment(taskComment)
        
    def setTaskDueDate(self, taskId, taskDueDate):
        task = self.__tasks[taskId]
        
        task.setDueDate(taskDueDate)

    def removeTask(self, taskId):
        self.__taskOrders.remove(taskId)
        
        return self.__tasks.pop(taskId, None)

    def editTaskTitle(self, taskId, newTitle):
        task = self.__tasks[taskId]

        task.editTitle(newTitle)
    
    def reorderTaskInSameSection(self, taskId, taskOrder):
        self.__taskOrders.remove(taskId)
        self.__taskOrders.insert(taskOrder, taskId)
        

