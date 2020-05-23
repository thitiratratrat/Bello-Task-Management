from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from BoardListWidget import *

class DisplayBoardBox(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(480, 350)
        self.listWidget = QListWidget()
        self.listWidget.setSpacing(10)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listWidget)
        self.listWidget.setIconSize(QSize(200, 80))
        self.listWidget.setFont(QFont("Moon", 10))
        self.setLayout(self.layout)
        self.boardDict = {}
        self.i = 1

    def createBox(self, boardDict):
        self.boardDict.update(boardDict)
        for boardId, boardTitle in boardDict.items():
            self.boardId = boardId
            self.boardTitle = boardTitle
            self.ran_num1 = randint(0, 150)
            self.ran_num2 = randint(0, 199)
            self.ran_num3 = randint(0, 226)
            self.board = BoardListWidget()
            self.board.setId(boardId)
            self.board.setBackground(
                QColor(self.ran_num1, self.ran_num2, self.ran_num3))
            self.board.setSizeHint(QSize(120, 80))
            self.board.setFont(QFont("Century Gothic", 12, QFont.Bold))
            self.board.setTextColor("white")
            self.board.setTextAlignment(Qt.AlignLeft)
            self.board.setText(self.boardTitle)
            self.addToListWidget(self.board)

    # def getKey(self,val):
    #     for key, value in self.boardDict.items(): 
    #      if val == value: 
    #          return key 

    def getBoardTitle(self):
        return self.listWidget.currentItem().text()

    def getSelectItemInBoardId(self):
        boardId = self.listWidget.currentItem().getId()
        
        return boardId

    def addToListWidget(self, board):
        self.i += 1
        self.listWidget.insertItem(self.i, board)
