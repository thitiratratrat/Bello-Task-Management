import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from dialogBox import * 

class SignUpWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setColor()
        self.usernameLabelSignUp = QLabel("Username: ")
        self.usernameLabelSignUp.setFont(
            QFont("Century Gothic", 11, QFont.Bold))
        self.usernameValueSignUp = QLineEdit()
        self.passwordLabelSignUp = QLabel("Password: ")
        self.passwordLabelSignUp.setFont(
            QFont("Century Gothic", 11, QFont.Bold))
        self.passwordValueSignUp = QLineEdit()
        self.confirmPasswordLabel = QLabel("Confirm Password: ")
        self.confirmPasswordLabel.setFont(
            QFont("Century Gothic", 11, QFont.Bold))
        self.usernameLabelSignUp.setStyleSheet("color: white")
        self.passwordLabelSignUp.setStyleSheet("color: white")
        self.confirmPasswordLabel.setStyleSheet("color:white")
        self.confirmPasswordValue = QLineEdit()
        self.signUpBtn = QPushButton("SIGN UP")
        self.signUpBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")
        self.signUpBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.signUpBtn.setFixedSize(100, 30)
        self.formSignUpLayout = QFormLayout()
        self.gridSignUpLayout = QGridLayout()
        self.usernameLabelSignUp.setContentsMargins(30, 30, 10, 15)
        self.usernameValueSignUp.setContentsMargins(0, 30, 30, 15)
        self.formSignUpLayout.addRow(
            self.usernameLabelSignUp, self.usernameValueSignUp)
        self.passwordLabelSignUp.setContentsMargins(30, 0, 10, 15)
        self.passwordValueSignUp.setContentsMargins(0, 0, 30, 15)
        self.formSignUpLayout.addRow(
            self.passwordLabelSignUp, self.passwordValueSignUp)
        self.confirmPasswordLabel.setContentsMargins(30, 0, 10, 20)
        self.confirmPasswordValue.setContentsMargins(0, 0, 30, 20)
        self.formSignUpLayout.addRow(
            self.confirmPasswordLabel, self.confirmPasswordValue)
        self.gridSignUpLayout.addLayout(self.formSignUpLayout, 0, 0)
        self.gridSignUpLayout.addWidget(
            self.signUpBtn, 1, 0, 1, 1, Qt.AlignCenter)
        self.setLayout(self.gridSignUpLayout)

    def showUsernameAlreadyExists(self):
        createDialogBox(self,"Error","ERROR: This username already exists.")

    def showComfirmPasswordMismatch(self):
        createDialogBox(self,"Error","ERROR: Your password doesn't match with comfirm password")
    
    def showInvalidPasswordLength(self):
        createDialogBox(self,"Error","ERROR: Passwords must be at least 4 characters")

    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor(82, 113, 159))
        self.setPalette(self.palette)
