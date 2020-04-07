import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MenuBar import *
from dialogBox import *  
import random

class TaskWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)


class Section(QListWidget): # addtask is here
    def __init__(self):
        QListWidget.__init__(self, None)
        self.setFixedSize(200, 480)


class SectionWidget(QWidget):
    def __init__(self, parent=None):
        super(SectionWidget, self).__init__(None)
        self.section = Section() #QListWidget
        self.colorLst = ['#9D9797','#52719F','#31446F']
        self.setColorSection = random.choice(self.colorLst)

        self.sectionTitleLayout = QHBoxLayout()
        self.sectionTitle = QLabel(" Sectioname")
        self.sectionTitle.setStyleSheet("color:white")

        self.editSectionTitleBtn = QToolButton()
        self.editSectionTitleBtn.setStyleSheet("background-color:rgb(250,231,110)")
        self.editSectionTitleBtn.setIcon(QIcon('images/edit.png'))
        self.editSectionTitleBtn.clicked.connect(self.showCreateSection)
        
        self.sectionTitle.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.sectionTitleLayout.addWidget(self.sectionTitle)
        self.sectionTitleLayout.addWidget(self.editSectionTitleBtn)

        self.mainSectionLayout = QVBoxLayout()
        self.mainSectionLayout.addLayout(self.sectionTitleLayout)
        self.mainSectionLayout.addWidget(self.section)
        self.setColor(self.setColorSection)
        self.setLayout(self.mainSectionLayout)

    def showCreateSection(self):
        self.newTitleAndDialogBox = createAddDialog(self,'Edit section title','Section name: ', 'Save',self.editTitleBtnFunc)

    def editTitleBtnFunc(self):
        self.newSectionTitle = self.newTitleAndDialogBox[0].text()
        self.editTitle(self.newSectionTitle)
        self.closeDialogBox()

    def editTitle(self,sectionTitle):
        self.sectionTitle.setText(sectionTitle)

    def closeDialogBox(self):
        self.newTitleAndDialogBox[1].reject()

    def setColor(self,colorName):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor('#52719F'))
        self.setPalette(self.palette)    

class BoardDetailPage(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.menuBar = MenuBar()
        self.sectionLayout = QHBoxLayout()
        self.widget = QWidget()
        for i in range(5):
            self.sectionWidget = SectionWidget()
            self.sectionLayout.addWidget(self.sectionWidget)
        self.addSectionBtn = QPushButton("Add section")
        self.addSectionBtn.setIcon(QIcon('images/add1.png'))
        self.addSectionBtn.setStyleSheet("background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.addSectionBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addSectionBtn.clicked.connect(self.crateNewSectionToBoard)

        self.deleteSectionBtn = QPushButton("Delete section")
        self.deleteSectionBtn.setStyleSheet("background-color:rgb(210,39,62); color:white")
        self.deleteSectionBtn.setIcon(QIcon('images/delete.png'))
        self.deleteSectionBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.deleteSectionBtn.clicked.connect(self.deleteSectionFromBoard)

        self.widget.setLayout(self.sectionLayout)        
        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

        self.sectionAndAddBtnLayout = QGridLayout()
        self.sectionAndAddBtnLayout.addWidget(self.scrollArea,0,0,4,1)
        self.sectionAndAddBtnLayout.addWidget(self.addSectionBtn,0,1,1,1)
        self.sectionAndAddBtnLayout.addWidget(self.deleteSectionBtn,1,1,1,1)

        self.boardDetailLayout = QVBoxLayout()
        self.boardDetailLayout.addWidget(self.menuBar)
        self.boardDetailLayout.addLayout(self.sectionAndAddBtnLayout)
        self.setLayout(self.boardDetailLayout)
    
    def crateNewSectionToBoard(self):
        self.newSectionWidget = createAddDialog(self,"create new section","Section name:","Create",self.addSectionToWidget)

    def getSectionNameFromDialog(self):
        self.sectionTitileFromDialog = self.newSectionWidget[0].text()
        
    def addSectionToWidget(self):
        self.getSectionNameFromDialog()
        self.sectionWidget = SectionWidget()
        self.sectionWidget.editTitle(self.sectionTitileFromDialog)
        self.sectionLayout.addWidget(self.sectionWidget)
        self.closeDialogBox()
    
    def deleteSectionFromBoard(self):
        self.selectedSectionToDelete = createAddDialog(self,"delete section","Section name:","Delete",self.deleteSection)
    
    def deleteSection(self):
        print("delete")



    def closeDialogBox(self):
        self.newSectionWidget[1].reject()

def main():
    app = QApplication(sys.argv)
    w = BoardDetailPage()
    w.resize(640, 480)
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
