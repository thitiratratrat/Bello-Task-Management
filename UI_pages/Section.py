import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Section(QListWidget): # addtask is here
    def __init__(self,parent= None):
        super(Section, self).__init__(parent)
        self.setFixedSize(200, 420)

class TaskWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, parent)


