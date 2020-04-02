import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class SignUpWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setColor()
        self.username_label = QLabel("Username: ")
        self.username_label.setFont(QFont("Century Gothic", 11,QFont.Bold))
        self.username_lineEdit = QLineEdit()
        self.password_label = QLabel("Password: ")
        self.password_label.setFont(QFont("Century Gothic", 11,QFont.Bold))
        self.password_lineEdit = QLineEdit()
        self.confirm_pass_label = QLabel("Confirm Password: ")
        self.confirm_pass_label.setFont(QFont("Century Gothic", 11,QFont.Bold))
        self.username_label.setStyleSheet("color: white")
        self.password_label.setStyleSheet("color: white")
        self.confirm_pass_label.setStyleSheet("color:white")
        self.confirm_pass_lineEdit = QLineEdit()
        self.signup_btn = QPushButton("SIGN UP")
        self.signup_btn.setStyleSheet("background-color:rgb(250,231,110);color:rgb(49,68,111)")
        self.signup_btn.clicked.connect(self.signUP)
        self.isHasUser = False
        self.signup_btn.setFont(QFont("Moon", 10,QFont.Bold))
        self.signup_btn.setFixedSize(100,30)
        self.signup_layout = QFormLayout()
        self.grid_signup_layout = QGridLayout()
        self.username_label.setContentsMargins(30,30,10,15)
        self.username_lineEdit.setContentsMargins(0,30,30,15)
        self.signup_layout.addRow(self.username_label, self.username_lineEdit)
        self.password_label.setContentsMargins(30,0,10,15)
        self.password_lineEdit.setContentsMargins(0,0,30,15)
        self.signup_layout.addRow(self.password_label, self.password_lineEdit)
        self.confirm_pass_label.setContentsMargins(30,0,10,20)
        self.confirm_pass_lineEdit.setContentsMargins(0,0,30,20)
        self.signup_layout.addRow(self.confirm_pass_label,self.confirm_pass_lineEdit)
        self.grid_signup_layout.addLayout(self.signup_layout,0,0)
        self.grid_signup_layout.addWidget(self.signup_btn,1,0,1,1,Qt.AlignCenter)
        self.setLayout(self.grid_signup_layout)
    def setColor(self):
        self.pal = QPalette()
        self.setAutoFillBackground(True)
        self.pal.setColor(QPalette.Window,QColor(82,113,159))
        self.setPalette(self.pal)
    def signUP(self):
        if(self.isHasUser == True):
            print("Success Sign Up")
        else:
            dialog = QDialog(self)
            dialog.setWindowTitle("Error")
            layout = QVBoxLayout()
            errMessage = QLabel(self)
            errMessage.setText("This number is already registered")
            close = QPushButton('Close')
            close.clicked.connect(dialog.close)
            layout.addWidget(errMessage)
            layout.addWidget(close)
            dialog.setLayout(layout)
            dialog.show()
            print("Error Message")