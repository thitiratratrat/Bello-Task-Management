import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from TabBar import * 
from TabWidget import *
from MenuBar import * 
from DisplayBoardBox import *

class DashboardPage(QWidget):
    def __init__(self,parent=None):
        super(DashboardPage,self).__init__(parent)
        self.parent = parent
        self.menuBar = MenuBar()
        self.menuBar.setFirstChaOfUsername("candy")
        self.menuBar.move(QPoint(0,0))
        self.tabBarBoard = TabWidget()
        self.tabBarBoard.setFixedSize(585,355)
        self.tabBarBoard.setFont(QFont("Moon",10,QFont.Bold))
        self.displayBoard = DisplayBoardBox()
        self.addBoardBtn = QPushButton("Add")
        self.addBoardBtn.setIcon(QIcon("images/add.png"))
        self.addBoardBtn.setStyleSheet("background-color:rgb(14,172,120);color:rgb(255,255,255)")
        self.addBoardBtn.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.addBoardBtn.clicked.connect(self.createNewBoard)
        self.deleteBoardBtn = QPushButton("Delete")
        self.deleteBoardBtn.setIcon(QIcon("images/delete.png"))
        self.deleteBoardBtn.setStyleSheet("background-color:rgb(210,39,62);color:rgb(255,255,255)")
        self.deleteBoardBtn.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.deleteBoardBtn.clicked.connect(self.deleteSelectBoard)
        self.tabBarBoard.addTab(self.displayBoard, QIcon("images/dashboard.png"), " Board")
        self.layout = QGridLayout()
        self.menuBar.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.menuBar, 0,0 )
        self.tabBarBoard.setContentsMargins(14,0,30,0)
        self.layout.addWidget(self.tabBarBoard,1,0,1,2)
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addStretch(1)
        self.btnLayout.addWidget(self.addBoardBtn)
        self.btnLayout.addWidget(self.deleteBoardBtn)
        self.layout.addLayout(self.btnLayout,2,0)
        self.setLayout(self.layout)
        self.show()
    
    def createNewBoard(self):
        self.createBoardDialog = QDialog(self)
        self.createBoardDialog.setWindowTitle("Create board")
        self.formLayout = QFormLayout()
        self.boardNameLabel = QLabel("Board Name: ")
        self.boardNameValue = QLineEdit(self)
        self.createBtn = QPushButton('Create')
        self.formLayout.addRow(self.boardNameLabel,self.boardNameValue)
        self.formLayout.addRow(self.createBtn)
        self.createBoardDialog.setLayout(self.formLayout)
        self.boardNameLabel.setFont(QFont("Century Gothic", 10))
        self.boardNameValue.setFont(QFont("Century Gothic",10))
        self.createBtn.setFont(QFont("Moon",10))
        self.createBtn.clicked.connect(self.createBtnAddBoard)
        self.createBoardDialog.show()

    def getBoardName(self):
        return self.boardNameValue.text()
    def addBoard(self,boardName):
        self.board = QListWidgetItem(QIcon(self.displayBoard.createBox()), boardName)
        self.displayBoard.addToListWidget(self.board)
        
    def createBtnAddBoard(self):
        if(self.boardNameValue.text() == ''):
            dialog = QDialog(self)
            dialog.setWindowTitle("Error")
            layout = QVBoxLayout()
            errMessage = QLabel(self)
            errMessage.setText("Error")
            close = QPushButton('Close')
            close.clicked.connect(dialog.close)
            layout.addWidget(errMessage)
            layout.addWidget(close)
            dialog.setLayout(layout)
            dialog.show()
        else:
            boardName = self.getBoardName()
            self.displayBoard.createBox(boardName)
            self.closeDialog()
    def closeDialog(self):
        self.createBoardDialog.reject()
    def deleteSelectBoard(self):
        self.select_board = self.displayBoard.listWidget.selectedItems()
        if not self.select_board:
            return
        for item in self.select_board:
            self.displayBoard.listWidget.takeItem(self.displayBoard.listWidget.row(item))
