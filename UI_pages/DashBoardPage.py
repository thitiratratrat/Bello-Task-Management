import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from TabWidget import *
from MenuBar import *
from DisplayBoardBox import *


class DashboardPage(QWidget):
    def __init__(self, parent):
        super(DashboardPage, self).__init__(parent)
        self.parent = parent
        self.createBtn = QPushButton()
        self.menuBar = MenuBar()
        self.tabBarBoard = TabWidget()
        self.tabBarBoard.setFont(QFont("Moon", 10, QFont.Bold))
        self.displayBoard = DisplayBoardBox()
        self.addBoardBtn = QPushButton("+ ADD board")
        self.addBoardBtn.clicked.connect(self.createNewBoard)
        self.deleteBoardBtn = QPushButton("- Delete board")
        self.deleteBoardBtn.clicked.connect(self.deleteSelectBoard)
        self.tabBarBoard.addTab(self.displayBoard, QIcon(
            "images/boardIcon.png"), " Board")
        self.tabBarBoard.addTab(QWidget(), "Team")
        self.layout = QGridLayout()
        self.menuBar.setContentsMargins(0, 0, 0, 20)
        self.layout.addWidget(self.menuBar, 0, 0)
        self.tabBarBoard.setContentsMargins(10, 0, 30, 0)
        self.layout.addWidget(self.tabBarBoard, 1, 0, 1, 2)
        self.layout.addWidget(self.addBoardBtn, 2, 1, 1, 2)
        self.layout.addWidget(self.deleteBoardBtn, 2, 2, 1, 2)
        self.setLayout(self.layout)
        self.show()

    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(61, 59, 59))
        paint.setBrush(QColor(61, 59, 59))
        paint.drawRect(0, 0, 640, 48)
        paint.end()

    def createNewBoard(self):
        self.createBoardDialog = QDialog(self)
        self.createBoardDialog.setWindowTitle("Create board")
        self.formLayout = QFormLayout()
        self.boardNameLabel = QLabel("Board Name: ")
        self.boardNameValue = QLineEdit(self)
        self.createBtn = QPushButton('Create')
        self.formLayout.addRow(self.boardNameLabel, self.boardNameValue)
        self.formLayout.addRow(self.createBtn)
        self.createBoardDialog.setLayout(self.formLayout)
        self.boardNameLabel.setFont(QFont("Century Gothic", 10))
        self.boardNameValue.setFont(QFont("Century Gothic", 10))
        self.createBtn.setFont(QFont("Moon", 10))
        self.createBtn.clicked.connect(self.createBtnAddBoard)
        self.createBoardDialog.show()

    def getBoardName(self):
        return self.boardNameValue.text()

    def addBoard(self, boardName):
        self.board = QListWidgetItem(
            QIcon(self.displayBoard.createBox()), boardName)
        self.displayBoard.addToListWidget(self.board)

    def createBtnAddBoard(self):
        boardName = self.getBoardName()
        self.board = QListWidgetItem(
            QIcon(self.displayBoard.createBox()), boardName)
        self.displayBoard.addToListWidget(self.board)
        self.closeDialog()

    def closeDialog(self):
        self.createBoardDialog.reject()

    def deleteSelectBoard(self):
        self.select_board = self.displayBoard.listWidget.selectedItems()
        if not self.select_board:
            return
        for item in self.select_board:
            self.displayBoard.listWidget.takeItem(
                self.displayBoard.listWidget.row(item))
