from typing import List
class Task:
    def __init__(self, title: str):
        self.__title = title
        self.__dueDate = None
        self.__image = None
        self.__responsibleMemberUsernames = []
        self.__comments = []
        self.__tags = []
    
    def getTitle(self) -> str:
        return self.__title
    
    def getResponsibleMemberUsernames(self) -> List[str]:
        return self.__responsibleMemberUsernames
    
    def getDueDate(self) -> str:
        return self.__dueDate
    
    def getComments(self) -> List[str]:
        return self.__comments
    
    def getTags(self) -> List[str]:
        return self.__tags
    
    def addTag(self, tag: str):
        self.__tags.append(tag)
        
    def removeTag(self, tag: str):
        self.__tags.remove(tag)
        
    def addComment(self, comment: str):
        self.__comments.append(comment)
        
    def addResponsibleMemberUsername(self, username: str):
        self.__responsibleMemberUsernames.append(username)
        
    def addDueDate(self, date: str):
        self.__dueDate = date
    
    def removeDueDate(self):
        self.__dueDate = None
    
        