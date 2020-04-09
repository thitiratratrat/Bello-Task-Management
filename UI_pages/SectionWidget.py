import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from Section import *
from dialogBox import * 
import random

class SectionWidget(QWidget):
    def __init__(self, parent=None):
        super(SectionWidget, self).__init__(None)
        self.section = Section() #QListWidget
        self.sectionId = None
        self.colorLst = ['#9D9797','#52719F','#31446F']
        self.setColorSection = random.choice(self.colorLst)
        self.sectionTitleLayout = QHBoxLayout()
        self.sectionTitle = QLabel(" Sectioname")
        self.sectionTitle.setStyleSheet("color:white")
        self.editSectionTitleBtn = QToolButton()
        self.editSectionTitleBtn.setStyleSheet("background-color:rgb(250,231,110)")
        self.editSectionTitleBtn.setIcon(QIcon('images/edit.png'))
        self.editSectionTitleBtn.clicked.connect(self.editSectionTitleDialog)
        self.index = None
        self.sectionTitle.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.sectionTitleLayout.addWidget(self.sectionTitle)
        self.sectionTitleLayout.addWidget(self.editSectionTitleBtn)

        self.mainSectionLayout = QVBoxLayout()
        self.mainSectionLayout.addLayout(self.sectionTitleLayout)
        self.mainSectionLayout.addWidget(self.section)
        self.setColor(self.setColorSection)
        self.setLayout(self.mainSectionLayout)

    def editSectionTitleDialog(self):
        self.newTitleAndDialogBox = createAddDialog(self,'Edit section title','Section name: ', 'Save')

    def getSectionTitle(self):
        return self.sectionTitle.text()
    
    def setSectionId(self, sectionId):
        self.sectionId = sectionId
    
    def getSectionId(self):
        return self.sectionId

    def setIndexSection(self,index):
        self.index = index

    def validateEditSectionTitle(self):
        if self.newTitleAndDialogBox[0].text() == '':
            createErrorDialogBox(self,"Error","Section title can not be empty")
            return False
        return True

    def editTitleBtnFunc(self):
        self.newSectionTitle = self.newTitleAndDialogBox[0].text()
        if self.newSectionTitle == '':
            self.showErrorSectionTitleEmpty()
        else:
            self.editTitle(self.newSectionTitle)
            self.closeEditDialogBox()

    def editTitle(self,sectionTitle):
        self.sectionTitle.setText(sectionTitle)

    def closeEditDialogBox(self):
        self.newTitleAndDialogBox[1].reject()

    def setColor(self,colorName):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        #self.palette.setColor(QPalette.Window, QColor(colorName))
        self.palette.setColor(QPalette.Window, QColor('#52719F'))
        self.setPalette(self.palette) 