from typing import List

class Board:
    def __init__(self, title: str):
        self.__title = title
        self.__id = None
        self.__sections = []
        self.__memberUsernames = []
        
    def getId(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
        
    def getMemberUsernames(self) -> List[str]:
        return self.__memberUsernames
    
    def getSections(self):
        return self.__sections
    
    def removeSection(sectionName: str):
        pass
    
        