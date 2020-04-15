import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from dialogBox import * 
from CustomDialog import *
from Section import *
from TaskWidget import *

class SectionWidget(QWidget):
    def __init__(self, parent):
        super(SectionWidget, self).__init__(parent)
        self.parent =parent

        self.boardId = None
        self.sectionId = None
        self.sectionIndex = 0
        self.section = QListWidget(self)

        self.section.setFixedSize(200, 420)

        self.sectionTitleLayout = QHBoxLayout()
        self.sectionTitle = QLabel("Sectioname")
        self.sectionTitle.setStyleSheet("color:white")
        self.editSectionTitleBtn = QToolButton()
        self.editSectionTitleBtn.setStyleSheet(
            "background-color:rgb(250,231,110)")
        self.editSectionTitleBtn.setIcon(QIcon('images/edit.png'))

        self.deleteSectionBtn = QToolButton()
        self.deleteSectionBtn.setStyleSheet(
            "background-color:rgb(210,39,62); color:white")
        self.deleteSectionBtn.setIcon(QIcon('images/delete.png'))

        self.deleteSectionBtn.clicked.connect(self.deleteSection)

        self.editSectionTitleDialog = CustomDialog(
            self, 'Edit section title', 'Section name: ', 'Save')
        self.editSectionTitleBtn.clicked.connect(
            self.showEditSectionTitleDialog)
        self.editSectionTitleDialog.button.clicked.connect(
            self.handleEditSectionTitleBtn)
        
        self.createTaskTitleDialog = CustomDialog(
            self, 'Create new task', 'Task name: ', 'Create')
        self.createTaskTitleDialog.button.clicked.connect(self.createTask)

        self.addTaskBtn =  QPushButton("Add task")
        self.addTaskBtn.setIcon(QIcon('images/add1.png'))
        self.addTaskBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.addTaskBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addTaskBtn.clicked.connect(self.createTaskDialog)

        self.sectionTitle.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.sectionTitleLayout.addWidget(self.sectionTitle)
        self.sectionTitleLayout.addWidget(self.editSectionTitleBtn)
        self.sectionTitleLayout.addWidget(self.deleteSectionBtn)

        self.mainSectionLayout = QVBoxLayout()
        self.mainSectionLayout.addLayout(self.sectionTitleLayout)
        self.mainSectionLayout.addWidget(self.section)
        self.mainSectionLayout.addWidget(self.addTaskBtn)
        self.setColor()
        self.setLayout(self.mainSectionLayout)

    def showEditSectionTitleDialog(self):
        self.editSectionTitleDialog.show()

    def setBoardId(self, boardId):
        self.boardId = boardId
    
    def setSectionId(self, sectionId):
        self.sectionId = sectionId
    
    def setSectionIndex(self,sectionIndex):
        self.sectionIndex = sectionIndex

    def getSectionTitle(self):
        return self.sectionTitle.text()

    def getSectionId(self):
        return self.sectionId

    def getNewSectionTitle(self):
        return self.editSectionTitleDialog.lineEdit.text()

    def getSectionIndex(self):
        return self.sectionIndex

    def handleEditSectionTitleBtn(self):
        if not self.validateNewSectionTitle():
            return

        newSectionTitle = self.getNewSectionTitle()

        self.editTitle(newSectionTitle)
        self.closeEditDialogBox()
        
        self.parent.parent.editSectionTitle(self.getSectionId(), self.getSectionTitle())

    def validateNewSectionTitle(self):
        newSectionTitle = self.getNewSectionTitle()
        if (len(newSectionTitle)!= 0 ):
            return True
        else:
            createErrorDialogBox(self,"Error","Section title can't be null")
            return False

    def editTitle(self, newSectionTitle):
        self.sectionTitle.setText(newSectionTitle)

    def closeEditDialogBox(self):
        self.editSectionTitleDialog.close()

    def setIndexSection(self, index):  # for delete
        self.index = index

    def deleteSection(self):
        index = self.getSectionIndex()
        sectionId = self.parent.deleteSection(index)
    
    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor('#52719F'))
        self.setPalette(self.palette)

    def createTaskDialog(self):
        self.createTaskTitleDialog.show()

    def createTask(self):
        if(not self.validateTaskTitle()):
            return
        self.createTaskTitleDialog.reject()
        title = self.createTaskTitleDialog.lineEdit.text()
        self.addTask(title)
        
    
    def validateTaskTitle(self):
        if self.createTaskTitleDialog.lineEdit.text() == '':
            createErrorDialogBox(
                self, "Error", "Task titile can not be empty")
            return False
        return True

    def addTask(self,taskTitle):
        self.taskWidget = TaskWidget(self)
        self.taskWidget.setTaskTitle(taskTitle)
        self.taskItem = QListWidgetItem(self.section)
        self.taskItem.setSizeHint(self.taskWidget.sizeHint())
        self.section.addItem(self.taskItem)
        self.section.setItemWidget(self.taskItem,self.taskWidget)