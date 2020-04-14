from typing import List


class Task:
    def __init__(self, title, id, dueDate=None, reponsibleMemberUsernames=set(), comments=[], tags=[]):
        self.__id = id
        self.__title = title
        self.__dueDate = dueDate
        self.__image = None
        self.__responsibleMemberUsernames = reponsibleMemberUsernames
        self.__comments = comments
        self.__tags = tags

    def getId(self):
        return self.__id

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
        self.__responsibleMemberUsernames.add(username)

    def addDueDate(self, date: str):
        self.__dueDate = date

    def removeDueDate(self):
        self.__dueDate = None
