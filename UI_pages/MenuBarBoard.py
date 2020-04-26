import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from BelloUI import *

class MenuBarBoard(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(640, 40)
        self.homeBtn = QPushButton("Home")
        self.homeBtn.setIcon(QIcon('images/home1.png'))
        self.homeBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.homeBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        
        self.boardTitle = QLabel()
        self.boardTitle.setFont(QFont("Century Gothic", 9, QFont.Bold))
        self.boardTitle.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        
        self.memberLabel = QLabel("Member: ")
        self.memberLabel.setFont(QFont("Century Gothic", 9, QFont.Bold))
        self.memberLabel.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")

        self.memberWidget = QWidget()
        self.mainMemberLayout = QHBoxLayout()

        #self.memberWidget.setFixedSize(,40)

        self.member = QLabel("a")
        self.member1 = QLabel("b")
        self.member2 = QLabel("c")
        self.member3 = QLabel("a")
        self.member4 = QLabel("b")
        self.member5 = QLabel("c")
        self.member6 = QLabel("a")
        self.member7 = QLabel("b")
        self.member8 = QLabel("c")
        
        self.member.setStyleSheet("background-color: red")
        self.member1.setStyleSheet("background-color: green")
        self.member2.setStyleSheet("background-color: white")
        self.member3.setStyleSheet("background-color: red")
        self.member4.setStyleSheet("background-color: green")
        self.member5.setStyleSheet("background-color: white")
        self.member6.setStyleSheet("background-color: red")
        self.member7.setStyleSheet("background-color: green")
        self.member8.setStyleSheet("background-color: white")

        self.mainMemberLayout.addWidget(self.member)
        self.mainMemberLayout.addWidget(self.member1)
        self.mainMemberLayout.addWidget(self.member2)
        self.mainMemberLayout.addWidget(self.member3)
        self.mainMemberLayout.addWidget(self.member4)
        self.mainMemberLayout.addWidget(self.member5)
        self.mainMemberLayout.addWidget(self.member6)
        self.mainMemberLayout.addWidget(self.member7)
        self.mainMemberLayout.addWidget(self.member8)

        self.memberWidget.setLayout(self.mainMemberLayout)
        self.memberWidget.setContentsMargins(0,0,10,10)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.verticalScrollBar().setEnabled(False)
        self.scrollArea.horizontalScrollBar().setEnabled(True)
        self.scrollArea.setWidget(self.memberWidget)
        self.scrollArea.setFixedSize(170,20)

        self.firstChaOfUsername = QLabel("")
        self.firstChaOfUsername.setFont(QFont("Moon", 10, QFont.Bold))
        
        self.firstChaOfUsername.setStyleSheet("color:white")
        self.menuBarWidget = QHBoxLayout()
        self.menuBarWidget.addWidget(self.homeBtn)
        self.menuBarWidget.addSpacing(30)
        self.menuBarWidget.addWidget(self.boardTitle)
        self.menuBarWidget.addSpacing(30)
        self.menuBarWidget.addWidget(self.memberLabel)
        self.menuBarWidget.addSpacing(10)
        self.menuBarWidget.addWidget(self.scrollArea)
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

    def setBoardTitle(self,boardTitle):
        self.boardTitle.setText(boardTitle)

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
