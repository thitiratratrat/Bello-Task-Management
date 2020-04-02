from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint


class DisplayBoardBox(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listWidget)
        self.listWidget.setIconSize(QSize(200, 80))
        self.listWidget.setFont(QFont("Moon", 10))
        self.board1 = QListWidgetItem(QIcon(self.createBox()), "Bello")
        self.listWidget.insertItem(1, self.board1)
        self.setLayout(self.layout)
        self.i = 1

    def createBox(self):
        self.ranNum1 = randint(0, 255)
        self.ranNum2 = randint(0, 255)
        self.ranNum3 = randint(0, 255)
        self.recPainter = QPixmap(120, 80)
        self.recPainter.fill(
            QColor(self.ranNum1, self.ranNum2, self.ranNum3))
        return self.recPainter

    def addToListWidget(self, board):
        self.i += 1
        self.listWidget.insertItem(self.i, board)
