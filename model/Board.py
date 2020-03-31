

class Board:
    def __init__(self, title: str, id, sections={}, memberUsernames={}):
        self.__title = title
        self.__id = id
        self.__sections = sections
        self.__memberUsernames = memberUsernames

    def getId(self) -> int:
        return self.__id

    def getTitle(self) -> str:
        return self.__title

    def getMemberUsernames(self):
        return self.__memberUsernames

    def getSections(self):
        return self.__sections

    def removeSection(sectionName: str):
        pass
