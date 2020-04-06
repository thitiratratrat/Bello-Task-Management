import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def createDialogBox(parent, dialogBoxTitle, message):
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