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
        #print(self.parent.getSectionId())
        newSectionId =  self.parent.getSectionId()
        cardSource.setTaskSectionId(newSectionId)
        self.parent.sectionTaskLayout.addWidget(cardSource)

        #get the new taskWidget order after move the taskWidget to another section
        self.parent.setNewTaskWidgetOrder()
        event.setDropAction(Qt.MoveAction)
        event.accept()