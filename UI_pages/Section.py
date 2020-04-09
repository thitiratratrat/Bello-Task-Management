import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TaskWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)


class Section(QListWidget): # addtask is here
    def __init__(self):
        QListWidget.__init__(self, None)
        self.setFixedSize(200, 420)