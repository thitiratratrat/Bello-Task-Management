import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint

class MenuBar(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setFixedSize(640,40)
        self.homeBtn = QPushButton("Home")
        self.homeBtn.setIcon(QIcon('images/homeIcon.png'))
        self.homeBtn.setStyleSheet("background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.homeBtn.setFont(QFont("Century Gothic",8, QFont.Bold))
        self.boardBtn = QPushButton("Board")
        self.boardBtn.setIcon(QIcon('images/boardIcon.png'))
        self.boardBtn.setStyleSheet("background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.boardBtn.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.menubar_widget = QHBoxLayout()
        self.menubar_widget.addWidget(self.homeBtn)
        self.menubar_widget.addWidget(self.boardBtn)
        self.menubar_widget.addStretch(1)
        self.setLayout(self.menubar_widget)
    def paintEvent(self,e):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(248,215,60))
        paint.setBrush(QColor(248,215,60))
        paint.drawRect(0,0, 640,50)
        paint.end()
  