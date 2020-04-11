import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from Section import *
from dialogBox import * 
import random




class SectionWidget(QWidget):
    def __init__(self,parent =None):
        super(SectionWidget, self).__init__(None)
        self.parent = parent
        self.section = QListWidget()
        self.section.setFixedSize(200, 420)
        self.boardId =None
        self.sectionId = None
        self.colorLst = ['#9D9797','#52719F','#31446F']
        self.setColorSection = random.choice(self.colorLst)
        self.sectionTitleLayout = QHBoxLayout()
        self.sectionTitle = QLabel("Sectioname")
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
        self.setColor()
        self.setLayout(self.mainSectionLayout)
        
    def editSectionTitleDialog(self):
        self.newTitleAndDialogBox = createAddDialog(self,'Edit section title','Section name: ', 'Save')
        self.newTitleAndDialogBox[2].clicked.connect(self.editTitleBtnFunc)

    def setBoardId(self,boardId):
        self.boardId = boardId

    def getSectionTitle(self):
        return self.sectionTitle.text()

    def setSectionId(self, sectionId):
        self.sectionId = sectionId
    
    def getSectionId(self):
        return self.sectionId

    def editTitleBtnFunc(self):
        self.newSectionTitle = self.newTitleAndDialogBox[0].text()
        if self.newSectionTitle == '':
            createErrorDialogBox(self,"Error","Section title can not be empty")
            return 
        else:
            self.editTitle(self.newSectionTitle)
            self.closeEditDialogBox()

    def editTitle(self, sectionTitle):
        self.sectionTitle.setText(sectionTitle)

    def closeEditDialogBox(self):
        self.newTitleAndDialogBox[1].reject()

    def setIndexSection(self,index): #for delete
        self.index = index

    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        #self.palette.setColor(QPalette.Window, QColor(colorName))
        self.palette.setColor(QPalette.Window, QColor('#52719F'))
        self.setPalette(self.palette) 