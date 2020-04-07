import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from dialogBox import *
class LoginWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setColor()
        self.usernameLabelLogin = QLabel("Username: ")
        self.usernameLabelLogin.setFont(
            QFont("Century Gothic", 11, QFont.Bold))
        self.usernameValueLogin = QLineEdit()
        self.passwordLabelLogin = QLabel("Password: ")
        self.passwordLabelLogin.setFont(
            QFont("Century Gothic", 11, QFont.Bold))
        self.usernameLabelLogin.setStyleSheet("color: white")
        self.passwordLabelLogin.setStyleSheet("color: white")
        self.passwordValueLogin = QLineEdit()
        self.loginBtn = QPushButton("LOGIN")
        self.loginBtn.setFixedSize(100, 30)
        self.gridLoginLayout = QGridLayout()
        self.formLoginLayout = QFormLayout()
        self.usernameLabelLogin.setContentsMargins(30, 50, 10, 25)
        self.usernameValueLogin.setContentsMargins(0, 50, 30, 25)
        self.formLoginLayout.addRow(
            self.usernameLabelLogin, self.usernameValueLogin)
        self.passwordLabelLogin.setContentsMargins(30, 0, 10, 20)
        self.passwordValueLogin.setContentsMargins(0, 0, 30, 20)
        self.formLoginLayout.addRow(
            self.passwordLabelLogin, self.passwordValueLogin)
        self.loginBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.loginBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")
        self.gridLoginLayout.addLayout(self.formLoginLayout, 0, 0)
        self.gridLoginLayout.addWidget(
            self.loginBtn, 1, 0, 1, 1, Qt.AlignCenter)
        self.setLayout(self.gridLoginLayout)
    
    def showLoginError(self):
        #createErrorDialogBox(self,"Error","Username or Password is invalid")
        version_box = QMessageBox(self)
        version_box.setWindowTitle("New version available!")
        version_box.setText("Error")
        version_box.addButton("Download now", QMessageBox.AcceptRole)
        ret = version_box.exec_()
        '''self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Error")
        self.layout = QVBoxLayout()
        errMessage = QLabel(self)
        errMessage.setFont(QFont("Century Gothic", 8,QFont.Bold))
        errMessage.setStyleSheet("color:rgb(178,34,34)")
        errMessage.setText("Username or Password is invalid.")
        closeBtn = QPushButton('Close')
        closeBtn.setStyleSheet("background-color: rgb(250,231,111); color: rgb(49,68,111);")
        closeBtn.setFont(QFont("Century Gothic", 7, QFont.Bold))
        closeBtn.clicked.connect(dialog.close)
        layout.addWidget(errMessage)
        layout.addWidget(closeBtn)
        self.dialog.setLayout(self.layout)
        self.dialog.show()'''

    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor(82, 113, 159))
        self.setPalette(self.palette)
