from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint


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
        self.listWidget.itemSelectionChanged.connect(self.getSelectItem)
        self.boardDict = None
        self.i = 1

    def createBox(self, dictBoard):
        self.boardDict = dictBoard
        for boardID, boardTitle in dictBoard.items():
            self.boardID = boardID
            self.boardTitle = boardTitle
            self.ran_num1 = randint(0, 150)
            self.ran_num2 = randint(0, 199)
            self.ran_num3 = randint(0, 226)
            self.board1 = QListWidgetItem()
            self.board1.setBackground(
                QColor(self.ran_num1, self.ran_num2, self.ran_num3))
            self.board1.setSizeHint(QSize(120, 80))
            self.board1.setFont(QFont("Century Gothic", 12, QFont.Bold))
            self.board1.setTextColor("white")
            self.board1.setTextAlignment(Qt.AlignLeft)
            self.board1.setText(self.boardTitle)
            self.addToListWidget(self.board1)

    def getKey(self,val):
        for key, value in self.boardDict.items(): 
         if val == value: 
             return key 

    def getSelectItemInBoardID(self):
        boardID = self.getKey(self.listWidget.currentItem().text()
        return boardID
        
    def addToListWidget(self, board):
        self.i += 1
        self.listWidget.insertItem(self.i, board)
