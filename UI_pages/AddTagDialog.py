import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class AddTagDialog(QDialog):
    def __init__(self, parent=None):
        super(AddTagDialog, self).__init__(parent)
        self.parent = parent
        
        self.setWindowTitle("Create Tag")
        self.listColorCode = ["#87CEEB","#9370DB","#FFB6C1","#FA8072","#FFA500"]
    
        self.tagTitleLabel = QLabel("Create Tag")
        self.tagTitleLabel.setFont(QFont("Moon", 9 , QFont.Bold))
        self.tagTitleLabel.setContentsMargins(5,10,20,10)
        self.tagComboBox = QComboBox()
        self.tagComboBox.addItem(self.parent.createIconColor(self.listColorCode[0]), "blue")
        self.tagComboBox.addItem(self.parent.createIconColor(self.listColorCode[1]), "purple")
        self.tagComboBox.addItem(self.parent.createIconColor(self.listColorCode[2]), "pink")
        self.tagComboBox.addItem(self.parent.createIconColor(self.listColorCode[3]), "red")
        self.tagComboBox.addItem(self.parent.createIconColor(self.listColorCode[4]), "orange")
        
        self.tagComboBox.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.tagLineEdit = QLineEdit()
        
        self.saveCreateTagBtn = QPushButton("Save")
        self.saveCreateTagBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.saveCreateTagBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.tagTitleLabel,0,0)
        self.mainLayout.addWidget(self.tagComboBox,1,0)
        self.mainLayout.addWidget(self.tagLineEdit,1,1)
        self.mainLayout.addWidget(self.saveCreateTagBtn,2,0,1,0,Qt.AlignCenter)

        self.setLayout(self.mainLayout)
        self.setFixedSize(260,150)
    
    def getColorFromDialog(self,index):
        return self.listColorCode[index]
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AddTagDialog()
    w.show()
    sys.exit(app.exec_())