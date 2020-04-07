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
    
    def addSection(self,sectionName: str):
        self.__sections.update(sectionName)

    def removeSection(self,sectionName: str):
        self.__sections.remove(sectionName)

    def editSectionTitle(self,sectionName: str,newSectionName):
        self.__sections.remove(sectionName)
        self.__sections.update(newSectionName)
                


