import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MenuBar import *
from dialogBox import *
from CustomDialog import CustomDialog
from DueDateWidget import *
from SectionWidget import *

class BoardDetailPage(QWidget):
    def __init__(self, parent):
        super(BoardDetailPage, self).__init__(parent)
        self.parent = parent
        self.boardId = None
        self.menuBar = MenuBar()
        self.sectionLayout = QHBoxLayout()
        self.taskWidget = None
        self.widget = QWidget()
        self.dialogCreate = CustomDialog(
            self, "create new section", "Section name:", "Create")
        self.addSectionBtn = QPushButton("Add section")
        self.addSectionBtn.setIcon(QIcon('images/add1.png'))
        self.addSectionBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.addSectionBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))

        self.addSectionBtn.clicked.connect(self.createNewSectionDialog)

        self.widget.setLayout(self.sectionLayout)
        
        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

        self.sectionAndAddBtnLayout = QGridLayout()
        self.sectionAndAddBtnLayout.addWidget(self.scrollArea, 0, 0, 4, 1)
        self.sectionAndAddBtnLayout.addWidget(self.addSectionBtn, 0, 1, 1, 1)

        self.boardDetailLayout = QVBoxLayout()
        self.boardDetailLayout.addWidget(self.menuBar)
        self.boardDetailLayout.addLayout(self.sectionAndAddBtnLayout)
        self.setLayout(self.boardDetailLayout)

    def setBoardId(self, boardId):
        self.boardId = boardId

    def getBoardId(self):
        return self.boardId

    def getSectionNameFromDialog(self):
        return self.dialogCreate.lineEdit.text()
        
    def getSectioNameFromId(self,sectionId):
        for i in range(self.sectionLayout.count()):
            section = self.sectionLayout.itemAt(i).widget()
            sectionTitle = section.getSectionTitle()
            if(sectionId == section.getSectionId()):
                sectionTitle = section.getSectionTitle()
                return sectionTitle

    def createNewSectionDialog(self):
        self.dialogCreate.show()

    def closeCreateNewSectionDialog(self):
        self.dialogCreate.close()

    def createSection(self, sectionDict):
        boardId = sectionDict.get("boardId")
        sectionTitle = sectionDict.get("sectionTitle")
        sectionId = sectionDict.get("sectionId")
        self.setBoardId(boardId)
        index = self.sectionLayout.count()
        self.addSectionToWidget(sectionTitle, sectionId,index)

    def addSectionToWidget(self, sectionTitle, sectionId,index):
        self.sectionWidget = SectionWidget(self)
        self.sectionWidget.setSectionIndex(index)
        self.sectionWidget.setSectionId(sectionId)
        self.sectionWidget.editTitle(sectionTitle)
        self.sectionWidget.setBoardId(self.boardId)
        self.sectionLayout.addWidget(self.sectionWidget)
    
    def validateSectionTitle(self):
        if self.dialogCreate.lineEdit.text() == '':
            createErrorDialogBox(
                self, "Error", "Section title can not be empty")
            return False
        return True

    def initBoardDetail(self, boardDetailDict):
        boardId = boardDetailDict.get("boardId")
        self.setBoardId(boardId)
        boardDetailDict = boardDetailDict.get("boardDetail")
        boardMembers = boardDetailDict.get("members")
        sectionDict = boardDetailDict.get("sections")
        indexSection = 0 
        for sectionId, sectionAndTaskTitle in sectionDict.items():
            sectionTitleDict = sectionAndTaskTitle
            sectionTitle = sectionTitleDict.get("title")
            taskDict = sectionTitleDict.get("task")
            self.addSectionToWidget(sectionTitle, sectionId,indexSection)
            indexSection += 1
            for taskId, taskInfo in taskDict.items():
                taskInfoDict = taskInfo
                #print("Info: ", taskInfoDict)
                taskTitle = taskInfoDict.get("title")
                taskResponsibleMembers = taskInfoDict.get("responsibleMembers")
                taskDuedate = taskInfoDict.get("dueDate")
                taskComments = taskInfoDict.get("comments")
                taskTags = taskInfoDict.get("tags")
                taskState = taskInfoDict.get("isFinished")
                #TODO setTaskComment, setTaskRespon
                for i in range (self.sectionLayout.count()):
                    if( self.sectionLayout.itemAt(i).widget().getSectionId() == sectionId):
                        indexTask = self.sectionLayout.itemAt(i).widget().sectionTaskLayout.count()
                        self.sectionLayout.itemAt(i).widget().addTask(taskTitle, boardId, 
                            sectionId, taskId, indexTask,taskDuedate,taskState,taskTags,taskComments)

    def deleteSection(self,index):
        self.newWidget =  self.sectionLayout.takeAt(index).widget()
        self.newWidget.setParent(None)
        newIndex = self.sectionLayout.count()
        for index in range(newIndex):
            self.item = self.sectionLayout.itemAt(index).widget()
            self.item.setSectionIndex(index)
            
        self.parent.deleteSection(self.getBoardId(), self.newWidget.getSectionId())

    def deleteTask(self,index,sectionId):
        for i in range(self.sectionLayout.count()):
            if(self.sectionLayout.itemAt(i).widget().getSectionId() == sectionId):
                sectionWidget = self.sectionLayout.itemAt(i).widget()
                
                taskId = sectionWidget.sectionTaskLayout.itemAt(index).widget().getTaskId()

                self.parent.deleteTask(sectionId, taskId)

                sectionWidget.sectionTaskLayout.takeAt(index).widget().deleteLater()
                
                newIndex = sectionWidget.sectionTaskLayout.count()
                
                for index in range(newIndex):
                    self.item = sectionWidget.sectionTaskLayout.itemAt(index).widget()
                    self.item.setTaskIndex(index)

    def clearAllSection(self):
        for i in reversed(range(self.sectionLayout.count())): 
            self.sectionLayout.itemAt(i).widget().deleteLater()
    
    def createNewTask(self,taskDict):
        boardId = taskDict.get("boardId")
        sectionId = taskDict.get("sectionId")
        taskId = taskDict.get("taskId")
        taskTitle = taskDict.get("taskTitle")
        taskDueDate = None
        taskState = False
        taskTag = {}
        taskComments = []
        for i in range (self.sectionLayout.count()):
            if( self.sectionLayout.itemAt(i).widget().getSectionId() == sectionId):
                index = self.sectionLayout.itemAt(i).widget().sectionTaskLayout.count()
                self.sectionLayout.itemAt(i).widget().addTask(taskTitle, boardId, 
                    sectionId, taskId, index,taskDueDate,taskState,taskTag,taskComments)
    
    