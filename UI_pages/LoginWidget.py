import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from BelloUI import *
from LoginSignUpPage import * 

class LoginWidget(QWidget):
    def __init__(self,parent):
        super(LoginWidget,self).__init__(parent)
        self.parent = parent
        self.setColor()
        self.username_label = QLabel("Username: ")
        self.username_label.setFont(QFont("Century Gothic", 11,QFont.Bold))
        self.username_lineEdit = QLineEdit()
        self.password_label = QLabel("Password: ")
        self.password_label.setFont(QFont("Century Gothic", 11,QFont.Bold))
        self.username_label.setStyleSheet("color: white")
        self.password_label.setStyleSheet("color: white")
        self.password_lineEdit = QLineEdit()
        self.login_btn = QPushButton("LOG IN")
        self.login_btn.clicked.connect(self.login)
        self.login_btn.setFixedSize(100,30)
        self.grid_login_layout = QGridLayout()
        self.login_layout = QFormLayout()
        self.username_label.setContentsMargins(30,50,10,25)
        self.username_lineEdit.setContentsMargins(0,50,30,25)
        self.login_layout.addRow(self.username_label, self.username_lineEdit)
        self.password_label.setContentsMargins(30,0,10,20)
        self.password_lineEdit.setContentsMargins(0,0,30,20)
        self.login_layout.addRow(self.password_label, self.password_lineEdit)
        self.login_btn.setFont(QFont("Moon", 10,QFont.Bold))
        self.login_btn.setStyleSheet("background-color:rgb(250,231,110);color:rgb(49,68,111)")
        self.grid_login_layout.addLayout(self.login_layout,0,0)
        self.grid_login_layout.addWidget(self.login_btn,1,0,1,1,Qt.AlignCenter)
        self.setLayout(self.grid_login_layout)
    def setColor(self):
        self.pal = QPalette()
        self.setAutoFillBackground(True)
        self.pal.setColor(QPalette.Window,QColor(82,113,159))
        self.setPalette(self.pal)
    def login(self):
        print("Login")
        self.parent.changetoDashPage()
        print("Done")
        