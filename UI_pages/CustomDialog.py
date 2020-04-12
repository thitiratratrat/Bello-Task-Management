from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class CustomDialog(QDialog):
    def __init__(self, parent, windowTitle, textLabel, textBtn):
        super().__init__(parent)

        self.setWindowTitle(windowTitle)
        self.button = QPushButton(textBtn)
        self.lineEdit = QLineEdit(parent)
        label = QLabel(textLabel)
        formLayout = QFormLayout()

        formLayout.addRow(label, self.lineEdit)
        formLayout.addRow(self.button)
        label.setFont(QFont("Century Gothic", 10, QFont.Bold))
        label.setStyleSheet("color:rgb(49,68,111)")
        self.setLayout(formLayout)
        self.lineEdit.setFont(QFont("Century Gothic", 10))
        self.button.setFont(QFont("Moon", 10, QFont.Bold))
        self.button.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")

