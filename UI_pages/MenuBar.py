import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from BelloUI import *

class MenuBar(QWidget):
    def __init__(self, parent= None):
        super(MenuBar, self).__init__(parent)
        self.parent =parent
        path= self.parent.parent.path
        self.setFixedSize(640, 40)
        self.homeBtn = QPushButton("Home")
        self.homeBtn.setIcon(QIcon(path + '\\home1.png'))
        self.homeBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.homeBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))

        self.firstChaOfUsername = QLabel("")
        self.firstChaOfUsername.setFont(QFont("Moon", 10, QFont.Bold))
        
        self.firstChaOfUsername.setStyleSheet("color:white")
        self.menuBarWidget = QHBoxLayout()
        self.menuBarWidget.addWidget(self.homeBtn)

        self.menuBarWidget.addStretch(1)
        self.menuBarWidget.addWidget(self.firstChaOfUsername)
        self.firstChaOfUsername.setContentsMargins(0, 0, 16, 0)
        self.rand_num1 = self.randomNum(0, 200)
        self.rand_num2 = self.randomNum(0, 199)
        self.rand_num3 = self.randomNum(0, 226)
        self.setLayout(self.menuBarWidget)

    def setFirstChaOfUsername(self, username):
        firstChaUsername = username[0]
        self.firstChaOfUsername.setText(firstChaUsername)

    def randomNum(self, start, end):
        self.rand_num = randint(start, end)
        return self.rand_num

    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(248, 215, 60))
        paint.setBrush(QColor(248, 215, 60))
        paint.drawRect(0, 0, 640, 50)
        paint.setPen(QColor(self.rand_num1, self.rand_num2, self.rand_num3))
        paint.setBrush(QColor(self.rand_num1, self.rand_num2, self.rand_num3))
        paint.drawEllipse(QPoint(610, 20), 15, 15)
        paint.end()
