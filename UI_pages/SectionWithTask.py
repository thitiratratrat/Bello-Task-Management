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

        isTaskIsSameSection = True
        cardSource=event.source()
        
        sectionId = cardSource.getTaskSectionId()
        newSectionId =  self.parent.getSectionId()

        if(newSectionId == sectionId):
            isTaskIsSameSection = True
        else: 
            isTaskIsSameSection = False

        cardSource.setTaskSectionId(newSectionId)
        self.parent.sectionTaskLayout.addWidget(cardSource)
        self.parent.setNewTaskWidgetOrder()
        
        boardId = self.parent.getSectionBoardId()
        taskId = cardSource.getTaskId()
        taskOrder = cardSource.getTaskIndex()
        
        if(isTaskIsSameSection):
            self.parent.parent.parent.reorderTaskInSameSection(boardId, sectionId, taskId, taskOrder)
        else:
            self.parent.parent.parent.reorderTaskInDifferentSection(boardId, sectionId, newSectionId, taskId, taskOrder)

        event.setDropAction(Qt.MoveAction)
        event.accept()