import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from CustomDialog import *
from dialogBox import *

class TaskWidget(QWidget):
    def __init__(self,parent =None):
        super(TaskWidget,self).__init__(parent)
        self.parent = parent
        self.taskTitle = QLabel("name")
        self.taskIndex = 0
        self.editTaskBtn = QToolButton() 
        self.editTaskBtn.setIcon(QIcon("images/editBtn.png"))
        self.editTaskBtn.clicked.connect(self.editTask)
        self.editTaskTitleDialog = CustomDialog(
            self, 'Edit task title', 'Task name: ', 'Save')
        self.editTaskTitleDialog.button.clicked.connect(self.handleEditSectionTitleBtn)

        self.deleteTaskBtn = QToolButton()
        self.deleteTaskBtn.setIcon(QIcon("images/deleteTask.png"))

        #self.tagColor = "tagColor"
        self.member = QLabel("C") 
        #self.member.setStyleSheet("border-radius:100;background-color:red")
        
        self.taskTitleAndEditLayout = QHBoxLayout()
        self.taskTitleAndEditLayout.addWidget(self.taskTitle)
        self.taskTitleAndEditLayout.addStretch(1)
        self.taskTitleAndEditLayout.addWidget(self.editTaskBtn)
        self.taskTitleAndEditLayout.addWidget(self.deleteTaskBtn)    

        self.taskLayout = QVBoxLayout()
        self.taskLayout.addLayout(self.taskTitleAndEditLayout)
        self.taskLayout.addWidget(self.member)

        self.setLayout(self.taskLayout)

    def setTaskTitle(self,newTaskTitle):
        self.taskTitle.setText(newTaskTitle)
    
    def setSectionIndex(self,taskIndex):
        self.taskIndex = taskIndex
    
    def getTaskTitle(self):
        return self.taskTitle.text()
    
    def getNewTaskTitle(self):
        return self.editTaskTitleDialog.lineEdit.text()

    def getTaskIndex(self):
        return self.taskIndex

    def editTask(self):
        self.editTaskTitleDialog.show()
    
    def handleEditSectionTitleBtn(self):
        if not self.validateNewTaskTitle():
            return
        newTaskTitle = self.getNewTaskTitle()

        self.setTaskTitle(newTaskTitle)
        self.closeEditDialogBox()

    def validateNewTaskTitle(self):
        newTaskTitle = self.getNewTaskTitle()
        if (len(newTaskTitle)!= 0 ):
            return True
        else:
            createErrorDialogBox(self,"Error","Task title can't be null")
            return False

    def closeEditDialogBox(self):
        self.editTaskTitleDialog.close()