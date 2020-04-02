import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint


class MenuBar(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        # self.setFixedSize(640,20)
        # self.setColor()
        # self.setContentsMargins(0,-5,30,0)
        self.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton("Home")
        self.homeBtn.setIcon(QIcon('images/homeIcon.png'))
        self.homeBtn.setStyleSheet(
            "background-color: rgb(87,85,85); color: white")
        self.homeBtn.setFont(QFont("Century Gothic", 8))
        self.boardBtn = QPushButton("Board")
        self.boardBtn.setIcon(QIcon('images/boardIcon.png'))
        self.boardBtn.setStyleSheet(
            "background-color: rgb(87,85,85); color: white")
        self.boardBtn.setFont(QFont("Century Gothic", 8))
        self.menubar_widget = QHBoxLayout()
        self.menubar_widget.addWidget(self.homeBtn)
        self.menubar_widget.addWidget(self.boardBtn)
        self.menubar_widget.addStretch(1)
        self.setLayout(self.menubar_widget)
