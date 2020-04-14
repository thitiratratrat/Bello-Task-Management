from typing import List


class Section:
    def __init__(self, title, id, tasks={}):
        self.__id = id
        self.__title = title
        self.__tasks = tasks

    def getId(self):
        return self.__id

    def getTitle(self) -> str:
        return self.__title

    def getTasks(self):
        return self.__tasks

    def editTitle(self, title):
        self.__title = title

    def addTask(self, task):
        self.__tasks[task.getId()] = task

    def removeTask(self, taskId):
        self.__tasks.pop(taskId, None)

    def editTaskTitle(self, taskId, newTitle):
        task = self.__tasks[taskId]

        task.editTitle(newTitle)

