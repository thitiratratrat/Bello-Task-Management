

class Board:
    def __init__(self, title, id, sections={}, memberUsernames=set()):
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

    def addMemberUsername(self, username):
        self.__memberUsernames.add(username)

    def getSections(self):
        return self.__sections

    def removeSection(sectionName: str):
        pass
