from typing import List
from Board import Board


class Member:
    def __init__(self):
        self.__account = None
        self.__boards = []
        self.__tasks = []
        self.__sections = []

    def createBoard(self, boardTitle: str):
        board = Board(boardTitle)
        self.__boards.append(board)

    def deleteBoard(self, boardId: int):
        self.__boards = list(filter(lambda board: (
            board.getId() != boardId), self.__boards))
