import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class MemberWidget(QDialog):
    def __init__(self,parent =None):
        super(MemberWidget,self).__init__(parent)
        self.parent = parent

        self.memberLabel = QLabel("Members")
        self.memberLabel.setFont(QFont("Moon", 10, QFont.Bold ))
        
        self.memberComboBox = QComboBox()
        self.memberComboBox.setFont(QFont("Century Gothic", 8 ))

        self.memberLayout = QHBoxLayout()
        self.memberNameLabel = QLabel("Member username: ")
        self.memberNameLabel.setFont(QFont("Century Gothic", 9))

        self.confirmMember = QLabel()
        self.confirmMember.setFont(QFont("Century Gothic", 9))

        self.memberLayout.addWidget(self.memberNameLabel)
        self.memberLayout.addWidget(self.confirmMember, 1, Qt.AlignLeft)

        self.saveBtn = QPushButton("Save")
        self.saveBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.saveBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")
        self.saveBtn.clicked.connect(self.addMemberToTask)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.memberLabel)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addWidget(self.memberComboBox)
        self.mainLayout.addSpacing(50)
        self.mainLayout.addLayout(self.memberLayout)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addWidget(self.saveBtn,1,Qt.AlignCenter)
        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)

    def addMemberToTask(self):
        memberUsername = self.memberComboBox.currentText()
        self.confirmMember.setText(memberUsername)

        return memberUsername
