import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from dialogBox import * 
from CustomDialog import *
from TaskWidget import *

class SectionWithTask(QWidget):
    def __init__(self, parent=None):
        super(SectionWithTask, self).__init__(parent)
        self.parent =parent
        self.setColor()
        self.setAcceptDrops(True)
        #self.setFixedSize(200,420)
     

    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor('white'))
        self.setPalette(self.palette)
    
    def dragEnterEvent(self, event):
        event.setDropAction(Qt.CopyAction)
        event.accept()
        
    def dropEvent(self, event):
        cardSource=event.source()
        self.parent.sectionTaskLayout.addWidget(cardSource)
        event.setDropAction(Qt.MoveAction)
        event.accept()

