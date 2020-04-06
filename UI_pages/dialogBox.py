import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def createErrorDialogBox(parent, dialogBoxTitle, message):
    dialog = QDialog(parent)
    dialog.setWindowTitle(dialogBoxTitle)
    layout = QVBoxLayout()
    errMessage = QLabel(parent)
    errMessage.setFont(QFont("Century Gothic", 8,QFont.Bold))
    errMessage.setStyleSheet("color:rgb(178,34,34)")
    errMessage.setText(message)
    closeBtn = QPushButton('Close')
    closeBtn.setStyleSheet("background-color: rgb(250,231,111); color: rgb(49,68,111);")
    closeBtn.setFont(QFont("Century Gothic", 7, QFont.Bold))
    closeBtn.clicked.connect(dialog.close)
    layout.addWidget(errMessage)
    layout.addWidget(closeBtn)
    dialog.setLayout(layout)
    dialog.show()

def createAddDialog(parent,windowTitle,txtLabel,txtBtn,funcConnect): #yung mai dai use na 
    lstReturnValue = []
    createBoardDialog = QDialog(parent)
    createBoardDialog.setWindowTitle(windowTitle)
    formLayout = QFormLayout()
    titleLabel = QLabel(txtLabel)
    titleValue = QLineEdit(parent)
    createBtn = QPushButton(txtBtn)
    formLayout.addRow(titleLabel, titleValue)
    formLayout.addRow(createBtn)
    createBoardDialog.setLayout(formLayout)
    lstReturnValue.append(titleValue)
    lstReturnValue.append(createBoardDialog)
    titleLabel.setFont(QFont("Century Gothic", 10,QFont.Bold))
    titleLabel.setStyleSheet("color:rgb(49,68,111)")
    titleValue.setFont(QFont("Century Gothic", 10))
    createBtn.setFont(QFont("Moon", 10,QFont.Bold))
    createBtn.setStyleSheet("background-color:rgb(250,231,110);color:rgb(49,68,111)")
    createBtn.clicked.connect(funcConnect)
    createBoardDialog.show()
    return lstReturnValue
