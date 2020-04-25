import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from AddTagDialog import * 
from dialogBox import * 

class TagWidget(QWidget):
    def __init__(self, parent=None):
        super(TagWidget, self).__init__(parent)
        self.parent =parent
        self.tagLabel = QLabel("TAGS")
        self.tagLabel.setContentsMargins(10,10,0,0)
        self.tagLabel.setFont(QFont("Moon",10, QFont.Bold))

        self.colorTag = {}
        self.addTagDialog = AddTagDialog(self)

        self.tagListAndBtnLayout = QHBoxLayout()
        self.tagListWidget = QListWidget()
        self.tagListWidget.setMovement(QListView.Static)
        #self.tagListWidget.setFixedSize(170,70)
        self.tagListWidget.setViewMode(QListWidget.IconMode)
        
        self.tagListWidget.setIconSize(QSize(50,30))
        self.tagListWidget.setFont(QFont("Century Gothic",8,QFont.Bold))

        self.addTagBtn = QPushButton("Add")
        self.addTagBtn.setIcon(QIcon("images/add.png"))
        self.addTagBtn.setStyleSheet(
            "background-color:rgb(14,172,120);color:rgb(255,255,255)")
        self.addTagBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addTagBtn.clicked.connect(self.showAddTagDialog)


        self.deleteTagBtn = QPushButton("Delete")
        self.deleteTagBtn.setIcon(QIcon("images/delete.png"))
        self.deleteTagBtn.setStyleSheet(
            "background-color:rgb(210,39,62);color:rgb(255,255,255)")
        self.deleteTagBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.deleteTagBtn.clicked.connect(self.deleteTagInList)

        self.addAndDeleteBtnLayout = QVBoxLayout()
        self.addAndDeleteBtnLayout.setAlignment(Qt.AlignTop)
        self.addAndDeleteBtnLayout.addWidget(self.addTagBtn)
        self.addAndDeleteBtnLayout.addWidget(self.deleteTagBtn)

        self.tagListAndBtnLayout.addWidget(self.tagListWidget)
        self.tagListAndBtnLayout.addLayout(self.addAndDeleteBtnLayout)

        self.addTagDialog.saveCreateTagBtn.clicked.connect(self.addTagInList)

        self.saveTagBtn = QPushButton("Save")
        self.saveTagBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.saveTagBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")
        
        self.mainTagLayout = QVBoxLayout()
        self.mainTagLayout.addWidget(self.tagLabel)
        self.mainTagLayout.addLayout(self.tagListAndBtnLayout)
        self.mainTagLayout.addWidget(self.saveTagBtn,1,Qt.AlignCenter)
       
        self.setLayout(self.mainTagLayout)

    def setColorCode(self,colorCode):
        self.colorCode = colorCode
    
    def setTagTitle(self,tagTitle):
        self.tagTitle = tagTitle

    def getTagTitle(self):
        return self.tagTitle
    
    def getTagLineEdit(self):
        tagTitle = self.addTagDialog.tagLineEdit.text()
        if(tagTitle == ""):
            createErrorDialogBox(self,"Error","Tag title can't be null")
            return False
        else:
            self.setTagTitle(tagTitle) 
            return tagTitle

    def getTagColor(self):
        return self.tagColor

    def getSelectedColor(self):
        index = self.addTagDialog.tagComboBox.currentIndex()
        colorCode =self.addTagDialog.getColorFromDialog(index)
        self.setColorCode(colorCode)
        return colorCode

    def createIconColor(self,colorCode):
        self.recPainter = QPixmap(60, 40)
        self.recPainter.fill(QColor(colorCode))
        return self.recPainter

    def showAddTagDialog(self):
        if(self.tagListWidget.count() < 3):
            self.addTagDialog.show()
        else:
            createErrorDialogBox(self, "Error","Your tags are reached the maximum")

    def addTagInList(self):
        colorCode = self.getSelectedColor()
        if(self.getTagLineEdit() == False  ):
            createErrorDialogBox(self, "Error","Your tag title can not be null")
            return
        elif(self.isAlreadyHasTag(self.getTagLineEdit(),colorCode) == 2):
            createErrorDialogBox(self, "Error","Tag title already in use")
            return
        elif(self.isAlreadyHasTag(self.getTagLineEdit(),colorCode) == 3):
            createErrorDialogBox(self, "Error","Tag color already in use")
            return
        else:
            self.tagItem = QListWidgetItem(QIcon(self.createIconColor(colorCode)), self.getTagLineEdit())
            self.tagListWidget.addItem(self.tagItem)
            self.colorTag[self.getTagLineEdit()] = colorCode
            self.addTagDialog.close()
    
    def isAlreadyHasTag(self,tagTitleLineEdit,tagColorBox):
        for tagTitle, tagColor in self.colorTag.items():
            if(tagTitle == tagTitleLineEdit ):
                return 2
            elif(tagColor == tagColorBox):
                return 3
        return 1
        
    def addTag(self,tagTitle,tagColor):
        self.tagItem = QListWidgetItem(QIcon(self.createIconColor(tagColor)),tagTitle)
        self.tagListWidget.addItem(self.tagItem)
        self.colorTag[tagTitle] = tagColor
        taskId= self.parent.parent.getTaskId()

    def deleteTagInList(self):
        self.selectTag = self.tagListWidget.selectedItems()
        if not self.selectTag:
            return
        for item in self.selectTag:
            self.tagListWidget.takeItem(
                self.tagListWidget.row(item))

            tagTitle = item.text()
            tagColor = self.colorTag.pop(item.text())

            taskId = self.parent.parent.getTaskId()

            self.parent.parent.parent.parent.parent.deleteTaskTag(taskId, tagTitle)
