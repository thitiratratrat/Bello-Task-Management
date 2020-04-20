import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from TabWidget import *
from DueDateWidget import *

class EditTaskDialog(QDialog):
    def __init__(self,parent =None):
        super(EditTaskDialog,self).__init__(parent)
        self.setWindowTitle("Edit task")
        self.parent = parent
        self.tabWidget = TabWidget()
        self.tabWidget.setFont(QFont("Moon", 8, QFont.Bold))

        self.dueDateWidget = DueDateWidget(self)
        self.dueDateWidget.saveDateBtn.clicked.connect(self.saveBtnInDueDate)

        self.tabWidget.addTab(QWidget(), QIcon(
            "images/editDialog.png"), " Edit")
        self.tabWidget.addTab(self.dueDateWidget, QIcon(
            "images/calendar.png"), " Due date")
        self.tabWidget.addTab(QWidget(), QIcon(
            "images/tag.png"), " Tag")

        self.mainEditTask = QVBoxLayout()
        self.mainEditTask.addWidget(self.tabWidget)
        self.setFixedSize(400,300)
        self.setLayout(self.mainEditTask)

    def saveBtnInDueDate(self):
        #TODO save duedate function
        print("---- save due date --- ")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EditTaskDialog()
    w.show()
    sys.exit(app.exec_())