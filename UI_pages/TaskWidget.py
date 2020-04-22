import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from dialogBox import *
from EditTaskDialog import * 
from TaskDetailDialog import *

class TaskWidget(QWidget):
    def __init__(self,parent =None):
        super(TaskWidget,self).__init__(parent)
        self.parent = parent
        self.setColor()
        self.taskSectionId = None
        self.taskBoardId = None
        self.taskId =None
        self.taskIndex = 0

        self.taskTitle = QLabel()
        self.taskTitle.setFont(QFont("Century Gothic",10,QFont.Bold))
        self.taskTitle.setStyleSheet("color: #31446F")
        
        self.editTaskBtn = QToolButton() 
        self.editTaskBtn.setIcon(QIcon("images/editBtn.png"))
        self.editTaskBtn.clicked.connect(self.editTask)
    
        self.deleteTaskBtn = QToolButton()
        self.deleteTaskBtn.setIcon(QIcon("images/deleteTask.png"))
        self.deleteTaskBtn.clicked.connect(self.deleteTask)

        self.editTaskDialog = EditTaskDialog(self)
        self.taskDetailDialog = TaskDetailDialog(self)
        
        '''self.taskDetailDialog.sectionTitleLabel.setText("in list " + 
            self.parent.parent.getSectionTitleFromId(self.getTaskSectionId()))'''

        self.taskDetailDialog.saveBtn.clicked.connect(self.getDataFromTaskDialog)
       
        self.dueDateLabel = QLabel()
        self.dueDateLabel.setFont(QFont("Century Gothic", 8, QFont.Bold))
      
        self.taskDetailDialog.dueDateCheckBox.setText("Due Date:  " +self.dueDateLabel.text())
     
        self.member = QLabel("c") 
        #self.member.setStyleSheet("border-radius:100;background-color:red")
        
        self.taskTitleAndEditLayout = QHBoxLayout()
        self.taskTitleAndEditLayout.addWidget(self.taskTitle)
        self.taskTitleAndEditLayout.addStretch(1)
        self.taskTitleAndEditLayout.addWidget(self.editTaskBtn)
        self.taskTitleAndEditLayout.addWidget(self.deleteTaskBtn)    

        self.tagLayout = QHBoxLayout()

        self.taskDueDateTagLayout = QHBoxLayout()
        self.taskDueDateTagLayout.addLayout(self.tagLayout)
        self.taskDueDateTagLayout.addWidget(self.dueDateLabel)
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

    def setDueDateLabel(self,newDueDate):
        return self.dueDateLabel.setText(newDueDate)
    
    def setTaskState(self,taskDueDate,taskState):
        if(taskDueDate != None):
            if(taskState == False):
                self.dueDateLabel.setStyleSheet("background-color:  #FA8072; color:white ")
            else:
                self.dueDateLabel.setStyleSheet("background-color:  #5FC083; color:white")

    def getTaskTitle(self):
        return self.taskTitle.text()
    
    def getTaskBoardId(self):
        return self.taskBoardId

    def getTaskId(self):
        return self.taskId 

    def getNewTaskTitle(self):
        return self.editTaskDialog.editTaskTitleDialog.lineEdit.text()

    def getTaskIndex(self):
        return self.taskIndex

    def getTaskSectionId(self):
        return self.taskSectionId
    
    def getDueDateLabel(self):
        return self.dueDateLabel.text()

    def getNewDate(self):
        newDate = self.editTaskDialog.dueDateWidget.date.text()
        self.dueDateLabel.setText(newDate[7:])
        self.setTaskState(self.getDueDateLabel(), False)
        self.parent.parent.parent.setTaskDueDate(self.getTaskId(),newDate[7:])
    
    def addTagLabel(self):
        listItem = [] 
        for i in range (self.editTaskDialog.tagWidget.tagListWidget.count()):
            tagItem = self.editTaskDialog.tagWidget.tagListWidget.item(i)
            self.tagColor = QToolButton()
            self.tagColor.setIcon(tagItem.icon())
            self.tagColor.setStyleSheet("background-color: rgba(0, 0, 0, 0%)")
            listItem.append(self.tagColor)
        self.addTagToWidget(listItem)
        

    def addTagToWidget(self,listItem):
        self.deleteAllTag()
        for item in range(len(listItem)):
            self.tagLayout.setSpacing(0.1)
            self.tagLayout.addWidget(listItem[item])
            taskId=  self.getTaskId()
            taskTagTitle = listItem[item].text() #error
            taskTagColor = self.editTaskDialog.tagWidget.colorTag[item]
            print("TagL ", taskTagTitle)
            #self.parent.parent.parent.addTaskTag(taskId,taskTagTitle , taskTagColor)

    def deleteAllTag(self):
        for i in reversed(range(self.tagLayout.count())): 
            self.tagLayout.itemAt(i).widget().deleteLater()
    
    def deleteTask(self):
        index = self.getTaskIndex()
        taskId = self.parent.deleteTask(index)

    def editTask(self):
        self.editTaskDialog.show()

    def validateNewTaskTitle(self):
        newTaskTitle = self.getNewTaskTitle()
        if (len(newTaskTitle)!= 0 ):
            return True
        else:
            createErrorDialogBox(self,"Error","Task title can't be null")
            return False
    
    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor('#FAE76E'))
        self.setPalette(self.palette)
    
    def mouseDoubleClickEvent(self,event):
        self.taskDetailDialog.show()

    def mouseMoveEvent(self, event):
        drag = QDrag(self)
        mimeData = QMimeData()
        drag.setMimeData(mimeData)
        dropAction = drag.start(Qt.CopyAction | Qt.MoveAction)

    def getDataFromTaskDialog(self):
        #getDueDateData
        self.state = self.taskDetailDialog.dueDateCheckBox.isChecked()
        self.setTaskState(self.getDueDateLabel(),self.state)
        self.parent.parent.parent.setTaskFinishState(self.getTaskId(),self.state)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaskWidget()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())