from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class BoardListWidget(QListWidgetItem):
    def __init__(self, parent=None):
        QListWidgetItem.__init__(self, None)
        self.__id = None
        
    def setId(self, id):
        self.__id = id
        
    def getId(self):
        return self.__id
        