from typing import List
from Board import Board


class Member:
    def __init__(self, username, boards={}, tasks={}, sections={}):
        self.__username = username
        self.__boards = boards
        self.__tasks = tasks
        self.__sections = sections

    def createBoard(self, boardTitle: str, boardId):
        board = Board(boardTitle, boardId)
        self.__boards[boardId] = board

    def deleteBoard(self, boardId):
        self.__boards.pop(boardId, None)
