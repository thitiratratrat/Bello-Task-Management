import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TaskDetailDialog(QDialog):
    def __init__(self,parent =None):
        super(TaskDetailDialog,self).__init__(parent)
        self.parent = parent

        self.dueDateCheckBox = QCheckBox("Due Date: ")
        self.enter = QPushButton("Save")

        self.mainTaskDetailLayout = QVBoxLayout()
        self.mainTaskDetailLayout.addWidget(self.dueDateCheckBox)
        self.mainTaskDetailLayout.addWidget(self.enter)
        self.setLayout(self.mainTaskDetailLayout)
        self.setFixedSize(400,400)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaskDetailDialog()
    w.show()
    sys.exit(app.exec_())
