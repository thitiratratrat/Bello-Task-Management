import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TaskDetailDialog(QDialog):
    def __init__(self,parent =None):
        super(TaskDetailDialog,self).__init__(parent)
        self.parent = parent

        self.taskTitleLabel = QLabel("kk")
        self.taskTitleLabel.setFont(QFont("Century-Gothic", 13, QFont.Bold))
        self.taskTitleLabel.setContentsMargins(20,20,0,0)
       
        self.sectionTitleLabel = QLabel("in list")
        self.sectionTitleLabel.setFont(QFont("Century-Gothic", 8))
        self.sectionTitleLabel.setContentsMargins(20,0,10,10)

        self.dueDateCheckBox = QCheckBox()
        self.dueDateCheckBox.setFont(QFont("Century-Gothic", 9, QFont.Bold))
        
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.saveBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")

        self.mainTaskDetailLayout = QVBoxLayout()
        self.mainTaskDetailLayout.addWidget(self.taskTitleLabel)
        self.mainTaskDetailLayout.addWidget(self.sectionTitleLabel)
        self.mainTaskDetailLayout.addWidget(self.dueDateCheckBox)
        self.mainTaskDetailLayout.addWidget(self.saveBtn,1,Qt.AlignCenter)
        self.setLayout(self.mainTaskDetailLayout)
        self.setFixedSize(400,400)
    
    '''
    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(248, 215, 60))
        paint.setBrush(QColor(248, 215, 60))
        paint.drawEllipse(QPoint(20, 350), 90, 90)
        paint.drawEllipse(QPoint(360, 140), 75, 75)
        paint.setPen(QColor(255, 160, 122))
        paint.setBrush(QColor(255, 160, 122))
        paint.drawPolygon([QPoint(60, 60), QPoint(140, 110), QPoint(130, 200)])
        paint.drawPolygon(
            [QPoint(379, 340),QPoint(180, 289), QPoint(240, 350) ])
        paint.end()'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaskDetailDialog()
    w.show()
    sys.exit(app.exec_())
