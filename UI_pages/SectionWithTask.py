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

        num = self.parent.sectionTaskLayout.count()

        if(num != 0 ):
            for i in range(num):
                if(event.pos().y()>=0 and event.pos().y() <= 79 ):
                    index = 0 
                    break
                elif(event.pos().y() >= 5*(num-(i+2))+69*(num-(i+1))+10 and event.pos().y()<= 5*(num-(i+1))+69*(num-i)+10):
                    index= num-(i+1)
                    break
                else:
                    index = num
        else:
            index = 0 
        
        sectionId = cardSource.getTaskSectionId()
        newSectionId =  self.parent.getSectionId()

        if(newSectionId == sectionId):
            isTaskIsSameSection = True
        else: 
            isTaskIsSameSection = False

        cardSource.setTaskSectionId(newSectionId)
        
        if (self.parent.sectionTaskLayout.count() == 0 ):
            self.parent.sectionTaskLayout.addWidget(cardSource)
        else: 
            self.parent.sectionTaskLayout.insertWidget(index, cardSource,0,Qt.AlignTop)

        self.parent.setNewTaskWidgetOrder()
        
        #boardId = self.parent.getSectionBoardId()
        taskId = cardSource.getTaskId()
        taskOrder = cardSource.getTaskIndex()
        
        if(isTaskIsSameSection):
            self.parent.parent.parent.reorderTaskInSameSection(sectionId, taskId, taskOrder)
        else:
            self.parent.parent.parent.reorderTaskInDifferentSection( sectionId, newSectionId, taskId, taskOrder)

        event.setDropAction(Qt.MoveAction)
        event.accept()