from typing import List

class Section:
    def __init__(self, title: str):
        self.__title = title
        self.__tasks = []

    def getTitle(self) -> str:
        return self.__title

    def getTasks(self) -> List[str]:
        return self.__tasks

    def addTask(self, task: str):
        self.__tasks.append(task)

    def removeTask(self, task: str):
        self.__tasks.remove(task)


    def editTaskTitle(self,task: str,newTitle: str):
        for i in range(len(self.__tasks)):
            if self.__tasks[i]==task:
                self.__tasks[i]=newTitle
            
            



