import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from dialogBox import * 
from CustomDialog import *
from SectionWithTask import *
from TaskWidget import *

class SectionWidget(QWidget):
    def __init__(self, parent=None):
        super(SectionWidget, self).__init__(parent)
        self.parent =parent
        self.taskWidget = None
        self.boardId = None
        self.sectionId = None
        self.sectionIndex = 0
        self.setFixedSize(230,380)

        self.section = SectionWithTask(self)
        self.scrollAreaTask = QScrollArea()

        self.sectionTaskLayout = QVBoxLayout()
        self.sectionTaskLayout.setAlignment(Qt.AlignTop)
        self.sectionTaskLayout.setContentsMargins(QMargins(5,10,5,10))
    
        self.section.setLayout(self.sectionTaskLayout)
        
        self.scrollAreaTask.setWidgetResizable(True)
        self.scrollAreaTask.setWidget(self.section)
        
        self.scrollAreaTask.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollAreaTask.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
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

        self.addTaskBtn =  QPushButton("Add task")
        self.addTaskBtn.setIcon(QIcon('images/add1.png'))
        self.addTaskBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.addTaskBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addTaskBtn.clicked.connect(self.createTaskDialog)
        self.createTaskTitleDialog.button.clicked.connect(self.validateTaskTitle)
        self.sectionTitle.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.sectionTitleLayout.addWidget(self.sectionTitle)
        self.sectionTitleLayout.addWidget(self.editSectionTitleBtn)
        self.sectionTitleLayout.addWidget(self.deleteSectionBtn)

        self.mainSectionLayout = QVBoxLayout()
        self.mainSectionLayout.addLayout(self.sectionTitleLayout)
        self.mainSectionLayout.addWidget(self.scrollAreaTask)
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

    def setIndexSection(self, index):  # for delete
        self.index = index

    def setNewTaskWidgetOrder(self):
        for i in range(self.sectionTaskLayout.count()):
            sectionId = self.sectionTaskLayout.itemAt(i).widget().getTaskSectionId()
            taskTitle = self.sectionTaskLayout.itemAt(i).widget().getTaskTitle()
            self.sectionTaskLayout.itemAt(i).widget().setTaskIndex(i)

    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor('#52719F'))
        self.setPalette(self.palette)
    
    def getSectionTitle(self):
        return self.sectionTitle.text()

    def getSectionBoardId(self):
        return self.boardId

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

    

    def deleteSection(self):
        index = self.getSectionIndex()
        sectionId = self.parent.deleteSection(index)
    
   

    def getCreateTaskTitle(self):
        return self.createTaskTitleDialog.lineEdit.text()

    def createTaskDialog(self):
        self.createTaskTitleDialog.show()
        
    def validateTaskTitle(self):
        taskTitle = self.getCreateTaskTitle()
        if taskTitle== "":
            createErrorDialogBox(
                self, "Error", "Task title can not be empty")
            return 
        boardId = self.parent.getBoardId()
        sectionId = self.getSectionId()
        taskOrder  = self.sectionTaskLayout.count()
        self.createTaskTitleDialog.close()

        self.parent.parent.createTask(boardId, sectionId, taskTitle,taskOrder)

    def addTask(self, taskTitle, boardId, sectionId, taskId, index,taskDueDate,taskState,taskTags):
        self.taskWidget = TaskWidget(self)
        self.taskWidget.setTaskId(taskId)
        self.taskWidget.setTaskSectionId(sectionId)
        self.taskWidget.setTaskBoardId(boardId)
        self.taskWidget.setTaskTitle(taskTitle)
        self.taskWidget.setTaskIndex(index)
        self.taskWidget.taskDetailDialog.taskTitleLabel.setText(taskTitle)
        if(taskState == True):
            self.taskWidget.taskDetailDialog.dueDateCheckBox.setChecked(taskState)
        self.taskWidget.setDueDateLabel(taskDueDate)
        self.taskWidget.setTaskState(taskDueDate,taskState)
        for tagTitle, tagColor in taskTags.items():
            self.taskWidget.editTaskDialog.tagWidget.addTag(tagTitle,tagColor)
            self.taskWidget.addTagInit()
        self.sectionTaskLayout.addWidget(self.taskWidget)

    def deleteTask(self,index):
        self.selectTask = self.sectionTaskLayout.takeAt(index).widget()
        self.selectTask.setParent(None)
        newIndex = self.sectionTaskLayout.count()

        for index in range(newIndex):
            self.item = self.sectionTaskLayout.itemAt(index).widget()
            self.item.setTaskIndex(index)
        
        #boardId = self.selectTask.getTaskBoardId()
        sectionId = self.selectTask.getTaskSectionId()
        taskId = self.selectTask.getTaskId()
            
        self.parent.parent.deleteTask(sectionId, taskId)

 