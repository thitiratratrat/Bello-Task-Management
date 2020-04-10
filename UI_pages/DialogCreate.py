from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class DialogCreate(QDialog):
    def __init__(self, parent, windowTitle, textLabel, textBtn):
        super().__init__(parent)

        self.setWindowTitle(windowTitle)
        self.createBtn = QPushButton(textBtn)
        self.titleLineEdit = QLineEdit(parent)
        titleLabel = QLabel(textLabel)
        formLayout = QFormLayout()

        formLayout.addRow(titleLabel, self.titleLineEdit)
        formLayout.addRow(self.createBtn)
        titleLabel.setFont(QFont("Century Gothic", 10, QFont.Bold))
        titleLabel.setStyleSheet("color:rgb(49,68,111)")
        self.setLayout(formLayout)
        self.titleLineEdit.setFont(QFont("Century Gothic", 10))
        self.createBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.createBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")

