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

        self.taskSectionId = None
        self.taskBoardId = None
        self.taskId =None
        self.taskIndex = 0

        self.taskTitle = QLabel("name")
        self.taskTitle.setFont(QFont("Century Gothic",10,QFont.Bold))
        self.taskTitle.setStyleSheet("color: #31446F")
        
        self.editTaskBtn = QToolButton() 
        self.editTaskBtn.setIcon(QIcon("images/editBtn.png"))
        self.editTaskBtn.clicked.connect(self.editTask)
        self.editTaskTitleDialog = CustomDialog(
            self, 'Edit task title', 'Task name: ', 'Save')
        self.editTaskTitleDialog.button.clicked.connect(self.handleEditSectionTitleBtn)

        self.deleteTaskBtn = QToolButton()
        self.deleteTaskBtn.setIcon(QIcon("images/deleteTask.png"))

        self.dueDateBtn = QPushButton("12-05-2020")
        self.tagColor = QPushButton("tag")

        self.member = QLabel("c") 
        #self.member.setStyleSheet("border-radius:100;background-color:red")
        
        self.taskTitleAndEditLayout = QHBoxLayout()
        self.taskTitleAndEditLayout.addWidget(self.taskTitle)
        self.taskTitleAndEditLayout.addStretch(1)
        self.taskTitleAndEditLayout.addWidget(self.editTaskBtn)
        self.taskTitleAndEditLayout.addWidget(self.deleteTaskBtn)    

        self.taskDueDateTagLayout = QHBoxLayout()
        self.taskDueDateTagLayout.addWidget(self.tagColor)
        self.taskDueDateTagLayout.addWidget(self.dueDateBtn)
        self.taskDueDateTagLayout.addStretch(1)
        self.taskDueDateTagLayout.addWidget(self.member)

        self.taskLayout = QVBoxLayout()
        self.taskLayout.addLayout(self.taskTitleAndEditLayout)
        self.taskLayout.addLayout(self.taskDueDateTagLayout)

        self.setLayout(self.taskLayout)

    def setTaskTitle(self,newTaskTitle):
        self.taskTitle.setText(newTaskTitle)
    
    def setTaskIndex(self,taskIndex):
        self.taskIndex = taskIndex
    
    def setTaskId(self,taskId):
        self.taskId = taskId

    def setTaskSectionId(self,taskSectionId):
        self.taskSectionId = taskSectionId

    def setTaskBoardId(self,taskBoardId):
        self.taskBoardId = taskBoardId

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaskWidget()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())