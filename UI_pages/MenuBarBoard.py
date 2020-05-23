import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from BelloUI import *

class MenuBarBoard(QWidget):
    def __init__(self,parent= None):
        super(MenuBarBoard, self).__init__(parent)
        self.parent =parent
        self.setFixedSize(640, 40)
        self.homeBtn = QPushButton("Home")
        path = self.parent.parent.path
        self.homeBtn.setIcon(QIcon(path + '\\home1.png'))
        self.homeBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.homeBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        
        self.boardTitle = QLabel()
        self.boardTitle.setFont(QFont("Century Gothic", 9, QFont.Bold))
        self.boardTitle.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        
        self.memberColor = ["#2E8B57", "#4682B4", "#B22222","#008080","#31446F"]
        self.memberLabel = QLabel("Member: ")
        self.memberLabel.setFont(QFont("Century Gothic", 9, QFont.Bold))
        self.memberLabel.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")

        self.mainMemberLayout = QHBoxLayout()
        
        self.member = QLabel()
        self.member.setFixedSize(25,20)
        self.member.setFont(QFont("Century Gothic", 7, QFont.Bold))

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
        self.menuBarWidget.addLayout(self.mainMemberLayout)

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

    def clearAllMember(self):
        for i in reversed(range(self.mainMemberLayout.count())): 
            self.mainMemberLayout.itemAt(i).widget().deleteLater()

    def addMemberInMenuBar(self,memberUsername ):
        member = QLabel("   "+ memberUsername[0]+" ")
        member.setFixedSize(25,20)
        member.setFont(QFont("Century Gothic", 7, QFont.Bold))
        member.setStyleSheet("background-color:"+self.memberColor.pop()+";  color: white")
        self.mainMemberLayout.addWidget(member)
        
    
    def addMainMember(self,username):
        self.member.setText("   " + username[0] + " ")
        self.member.setStyleSheet("background-color:"+self.memberColor.pop()+";  color: white")
        self.mainMemberLayout.addWidget(self.member)

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
