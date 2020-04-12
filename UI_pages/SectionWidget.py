import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from Section import *
from CustomDialog import *


class SectionWidget(QWidget):
    def __init__(self, parent, signal):
        super(SectionWidget, self).__init__(parent)
        self.signal = signal
        self.section = QListWidget()
        self.boardId = None
        self.sectionId = None

        self.section.setFixedSize(200, 420)

        self.sectionTitleLayout = QHBoxLayout()
        self.sectionTitle = QLabel("Sectioname")
        self.sectionTitle.setStyleSheet("color:white")
        self.editSectionTitleBtn = QToolButton()
        self.editSectionTitleBtn.setStyleSheet(
            "background-color:rgb(250,231,110)")
        self.editSectionTitleBtn.setIcon(QIcon('images/edit.png'))

        self.deleteSectionBtn = QToolButton()
        self.deleteSectionBtn.setStyleSheet(
            "background-color:rgb(210,39,62); color:white")
        self.deleteSectionBtn.setIcon(QIcon('images/delete.png'))

        self.editSectionTitleDialog = CustomDialog(
            self, 'Edit section title', 'Section name: ', 'Save')

        self.editSectionTitleBtn.clicked.connect(
            self.showEditSectionTitleDialog)
        self.editSectionTitleDialog.button.clicked.connect(
            self.handleEditSectionTitleBtn)
        self.index = None
        self.sectionTitle.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.sectionTitleLayout.addWidget(self.sectionTitle)
        self.sectionTitleLayout.addWidget(self.editSectionTitleBtn)
        self.sectionTitleLayout.addWidget(self.deleteSectionBtn)

        self.mainSectionLayout = QVBoxLayout()
        self.mainSectionLayout.addLayout(self.sectionTitleLayout)
        self.mainSectionLayout.addWidget(self.section)
        self.setColor()
        self.setLayout(self.mainSectionLayout)

    def showEditSectionTitleDialog(self):
        self.editSectionTitleDialog.show()

    def setBoardId(self, boardId):
        self.boardId = boardId

    def getSectionTitle(self):
        return self.sectionTitle.text()

    def setSectionId(self, sectionId):
        self.sectionId = sectionId

    def getSectionId(self):
        return self.sectionId

    def getNewSectionTitle(self):
        return self.editSectionTitleDialog.lineEdit.text()

    def handleEditSectionTitleBtn(self):
        if not self.validateNewSectionTitle():
            return

        newSectionTitle = self.getNewSectionTitle()

        self.editTitle(newSectionTitle)
        self.closeEditDialogBox()
        
        self.signal.signalDict.emit(
            {"sectionId": self.getSectionId(), "sectionTitle": self.getSectionTitle()})

    def validateNewSectionTitle(self):
        newSectionTitle = self.getNewSectionTitle()

        return True if len(newSectionTitle) != 0 else False

    def editTitle(self, newSectionTitle):
        self.sectionTitle.setText(newSectionTitle)

    def closeEditDialogBox(self):
        self.editSectionTitleDialog.close()

    def setIndexSection(self, index):  # for delete
        self.index = index

    def setColor(self):
        self.palette = QPalette()
        self.setAutoFillBackground(True)
        self.palette.setColor(QPalette.Window, QColor('#52719F'))
        self.setPalette(self.palette)
