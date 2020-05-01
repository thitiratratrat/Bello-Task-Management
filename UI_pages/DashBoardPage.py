import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from TabWidget import *
from MenuBar import *
from DisplayBoardBox import *
from dialogBox import *


class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super(DashboardPage, self).__init__(parent)
        self.parent = parent
        self.menuBar = MenuBar()
        self.createBtn = QPushButton('Create')
        self.menuBar.setFirstChaOfUsername("candy")
        self.menuBar.move(QPoint(0, 0))
        self.tabBarBoard = TabWidget()
        self.tabBarBoard.setFixedSize(585, 355)
        self.tabBarBoard.setFont(QFont("Moon", 10, QFont.Bold))
        self.displayBoard = DisplayBoardBox()
        self.addBoardBtn = QPushButton("Add")
        self.addBoardBtn.setIcon(QIcon("images/add.png"))
        self.addBoardBtn.setStyleSheet(
            "background-color:rgb(14,172,120);color:rgb(255,255,255)")
        self.addBoardBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addBoardBtn.clicked.connect(self.createNewBoard)
        self.deleteBoardBtn = QPushButton("Delete")
        self.deleteBoardBtn.setIcon(QIcon("images/delete.png"))
        self.deleteBoardBtn.setStyleSheet(
            "background-color:rgb(210,39,62);color:rgb(255,255,255)")
        self.deleteBoardBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.tabBarBoard.addTab(self.displayBoard, QIcon(
            "images/dashboard.png"), " Board")

        self.layout = QGridLayout()
        self.menuBar.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.menuBar, 0, 0)
        self.tabBarBoard.setContentsMargins(14, 0, 30, 0)
        self.layout.addWidget(self.tabBarBoard, 1, 0, 1, 2)
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addStretch(1)
        self.btnLayout.addWidget(self.addBoardBtn)
        self.btnLayout.addWidget(self.deleteBoardBtn)
        self.layout.addLayout(self.btnLayout, 2, 0)
        
        

        self.setLayout(self.layout)
        self.show()

    def createNewBoard(self):
        self.createBoardDialog = QDialog(self)
        self.createBoardDialog.setWindowTitle("Create board")
        self.formLayout = QFormLayout()
        self.boardTitleLabel = QLabel("Board Name: ")
        self.boardTitleValue = QLineEdit(self)
        self.formLayout.addRow(self.boardTitleLabel, self.boardTitleValue)
        self.formLayout.addRow(self.createBtn)
        self.createBoardDialog.setLayout(self.formLayout)
        self.boardTitleLabel.setFont(QFont("Century Gothic", 10,QFont.Bold))
        self.boardTitleLabel.setStyleSheet("color:rgb(49,68,111)")
        self.boardTitleValue.setFont(QFont("Century Gothic", 10))
        self.createBtn.setFont(QFont("Moon", 10,QFont.Bold))
        self.createBtn.setStyleSheet("background-color:rgb(250,231,110);color:rgb(49,68,111)")
        self.createBoardDialog.show()

    def getBoardTitle(self):
        return self.boardTitleValue.text()

    def addBoard(self, boardDict):
        self.displayBoard.createBox(boardDict)
    
    def deleteAllBoard(self):
        self.displayBoard.listWidget.clear()

    def validateBoardTitle(self):
        if self.boardTitleValue.text() == '':
            createErrorDialogBox(self,"Error","Board title cannot be empty")
            return False
        
        return True

    def showBoardTitleIsExist(self):
        createErrorDialogBox(self,"Error","Board title is already exist")

    def closeDialog(self):
        self.createBoardDialog.reject()

    def deleteSelectBoard(self):
        self.select_board = self.displayBoard.listWidget.selectedItems()
        self.selectItemId = self.displayBoard.getSelectItemInBoardId()
        if not self.select_board:
            return
        for item in self.select_board:
            self.displayBoard.listWidget.takeItem(
                self.displayBoard.listWidget.row(item))
        del self.displayBoard.boardDict[self.selectItemId]
        return self.selectItemId
    
    def deleteBoardId(self,boardId):
        for i in range(self.displayBoard.listWidget.count()):
            board = self.displayBoard.listWidget.item(i)
            id = self.displayBoard.getKey(board.text())

            if(id == boardId):
                selectItem = self.displayBoard.listWidget.takeItem(i)
                print("itemmmm---: ", selectItem)
                break
        print("---finished------")
                
        


