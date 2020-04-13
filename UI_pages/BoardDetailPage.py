import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MenuBar import *
from dialogBox import *
from CustomDialog import CustomDialog
from SectionWidget import *

class BoardDetailPage(QWidget):
    def __init__(self, parent, signal):
        super(BoardDetailPage, self).__init__(parent)
        self.parent = parent
        self.editSectionTitleSignal = signal
        self.boardId = None
        self.menuBar = MenuBar()
        self.sectionLayout = QHBoxLayout()
        self.sectionWidget = None
        self.widget = QWidget()
        self.dialogCreate = CustomDialog(
            self, "create new section", "Section name:", "Create")
        self.addSectionBtn = QPushButton("Add section")
        self.addSectionBtn.setIcon(QIcon('images/add1.png'))
        self.addSectionBtn.setStyleSheet(
            "background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.addSectionBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addSectionBtn.clicked.connect(self.createNewSectionDialog)

        self.widget.setLayout(self.sectionLayout)
        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

        self.sectionAndAddBtnLayout = QGridLayout()
        self.sectionAndAddBtnLayout.addWidget(self.scrollArea, 0, 0, 4, 1)
        self.sectionAndAddBtnLayout.addWidget(self.addSectionBtn, 0, 1, 1, 1)

        self.boardDetailLayout = QVBoxLayout()
        self.boardDetailLayout.addWidget(self.menuBar)
        self.boardDetailLayout.addLayout(self.sectionAndAddBtnLayout)
        self.setLayout(self.boardDetailLayout)

    def setBoardId(self, boardId):
        self.boardId = boardId

    def getBoardId(self):
        return self.boardId

    def getSectionNameFromDialog(self):
        return self.dialogCreate.lineEdit.text()

    def createNewSectionDialog(self):
        self.dialogCreate.show()

    def closeCreateNewSectionDialog(self):
        self.dialogCreate.close()

    def createSection(self, sectionDict):
        boardId = sectionDict.get("boardId")
        sectionTitle = sectionDict.get("sectionTitle")
        sectionId = sectionDict.get("sectionId")
        self.setBoardId(boardId)
        index = self.sectionLayout.count()
        self.addSectionToWidget(sectionTitle, sectionId,index)

    def addSectionToWidget(self, sectionTitle, sectionId,index):
        self.sectionWidget = SectionWidget(self, self.editSectionTitleSignal)
        self.sectionWidget.setSectionIndex(index)
        self.sectionWidget.setSectionId(sectionId)
        self.sectionWidget.editTitle(sectionTitle)
        self.sectionLayout.addWidget(self.sectionWidget)

    def validateSectionTitle(self):
        if self.dialogCreate.lineEdit.text() == '':
            createErrorDialogBox(
                self, "Error", "Board titile can not be empty")

            return False

        return True

    def initBoardDetail(self, boardDetailDict):
        self.setBoardId(boardDetailDict.get("boardId"))
        sectionDict = boardDetailDict.get("boardDetail")
        index = 0 
        for sectionId, sectionAndTaskTitle in sectionDict.items():
            sectionTitleDict = sectionAndTaskTitle
            sectionTitle = sectionTitleDict.get("title")
            self.addSectionToWidget(sectionTitle, sectionId,index)
            index += 1

    def deleteSectionTest(self,index):
        self.newWidget =  self.sectionLayout.takeAt(index).widget()
        self.newWidget.setParent(None)
        newIndex = self.sectionLayout.count()
        for index in range(newIndex):
            self.item = self.sectionLayout.itemAt(index).widget()
            self.item.setSectionIndex(index)
        return self.newWidget.getSectionId()
    
    def clearAllSection(self):
        for i in self.sectionLayout.count():
            widget = self.sectionLayout.takeAt(i).widget()
            widget.setParent(None)