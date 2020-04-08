from typing import List
from Board import Board
from Section import Section


class User:
    def __init__(self, username, boards={}):
        self.__username = username
        self.__boards = boards

    def getUsername(self):
        return self.__username

    def getBoards(self):
        return self.__boards

    def addBoard(self, board):
        self.__boards[board.getId()] = board

        board.addMemberUsername(self.__username)

    def createBoard(self, boardTitle: str, boardId):
        board = Board(boardTitle, boardId)

        self.addBoard(board)
        
    def addSection(self, boardId, sectionId, sectionTitle):
        board = self.__boards[boardId]
        section = Section(sectionTitle, sectionId)
    
        board.addSection(section)
        
    def removeSection(self, boardId, sectionId):
        board = self.__boards[boardId]
        
        board.removeSection(sectionId)
        
    def editSectionTitle(self, boardId, sectionId, sectionTitle):
        board = self.__boards[boardId]
        
        board.editSectionTitle(sectionId, sectionTitle)

    def deleteBoard(self, boardId):
        self.__boards.pop(boardId, None)
