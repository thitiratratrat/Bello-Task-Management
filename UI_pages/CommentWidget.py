import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class CommentWidget(QDialog):
    def __init__(self,parent =None):
        super(CommentWidget,self).__init__(parent)
        self.parent = parent

        self.nameAndSquare = QLabel("  C ")
        self.nameAndSquare.setFont(QFont("Moon",8,QFont.Bold))
        self.nameAndSquare.setStyleSheet("background-color: #FAE76E ;color:#31446F ")
        self.nameAndSquare.setFixedSize(20,20)

        self.userLabel = QLabel("candy")
        self.userLabel.setFont(QFont("Century Gothic",8,QFont.Bold))

        self.commentTxt = QLabel("okay")
        self.commentTxt.setFont(QFont("Century Gothic",7))

        self.mainLayout = QGridLayout()

        self.mainLayout.addWidget(self.nameAndSquare,0,0)
        self.mainLayout.addWidget(self.userLabel, 0,1)
        self.mainLayout.addWidget(self.commentTxt,1,1)
        self.setLayout(self.mainLayout)
        #self.setFixedSize(200,70)
    
    def setUser(self,userName):
        self.userLabel.setText(userName)
        self.nameAndSquare.setText("  "+ userName[0]+ " ")
    
    def setCommentTxt(self,commentTxt):
        self.commentTxt.setText(commentTxt)

    def getUser(self):
        return self.userLabel.text()
    
    def getComment(self):
        return self.commentTxt.text()
        