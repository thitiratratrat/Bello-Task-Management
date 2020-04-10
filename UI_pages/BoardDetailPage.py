import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MenuBar import *
from dialogBox import *  
from SectionWidget import * 

class BoardDetailPage(QWidget):
    def __init__(self, parent=None):
        super(BoardDetailPage, self).__init__(parent)
        self.parent = parent
        self.boardId = None
        self.menuBar = MenuBar()
        self.sectionLayout = QHBoxLayout()
        self.widget = QWidget()
        self.btn = QPushButton()
        #self.sectionWidget = SectionWidget()
        self.addSectionBtn = QPushButton("Add section")
        self.addSectionBtn.setIcon(QIcon('images/add1.png'))
        self.addSectionBtn.setStyleSheet("background-color: rgb(250,231,111); color: rgb(49,68,111)")
        self.addSectionBtn.setFont(QFont("Century Gothic", 8, QFont.Bold))
        self.addSectionBtn.clicked.connect(self.createNewSection)
       
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
    
    def setBoardId(self, boardId):
        self.boardId = boardId

    def getBoardId(self):
        return self.boardId

    def createNewSection(self):
        self.newSectionWidget = createAddDialog(self,"create new section","Section name:","Create")
        print(self.newSectionWidget[2])
        self.btn = self.newSectionWidget[2]
        print(self.btn)

    def createSection(self,sectionDict):
        boardId = sectionDict.get("boardId")
        sectionTitle = sectionDict.get("sectionTitle")
        sectionId = sectionDict.get("sectionId")
        self.setBoardId(boardId)
        self.addSectionToWidget(sectionTitle, sectionId)
    
    def addSectionToWidget(self,sectionTitle,sectionId):
        self.sectionWidget = SectionWidget()
        self.sectionWidget.setSectionId(sectionId)
        self.sectionWidget.editTitle(sectionTitle)
        self.sectionLayout.addWidget(self.sectionWidget)

    def validateSectionTitle(self):
        if self.newSectionWidget[0].text() == '':
            createErrorDialogBox(self,"Error","Board titile can not be empty")
            return False
        return True
    
    def initBoardDetail(self,boardDetailDict):
        self.setBoardId(boardDetailDict.get("boardId"))
        sectionDict = boardDetailDict.get("boardDetail")
        for sectionId,sectionAndTaskTitle in sectionDict.items():
            sectionTitleDict = sectionAndTaskTitle
            sectionTitle = sectionTitleDict.get("title")
            self.addSectionToWidget(sectionId,sectionTitle)

    def closeDialogBox(self):
        self.newSectionWidget[1].reject()

    def closeDeleteSectionBox(self):
        self.selectedSectionToDelete[1].reject()

    def deleteSectionFromBoard(self):
        self.selectedSectionToDelete = createAddDialog(self,"delete section","Section name:","Delete",self.deleteSection)
    
    def deleteSection(self):
        isDelete = False
        for i in range(self.sectionLayout.count()):
            if(self.sectionLayout.itemAt(i).widget().getSectionTitle() == self.selectedSectionToDelete[0].text()):
                self.sectionLayout.takeAt(i)
                isDelete = True
                self.closeDeleteSectionBox()
                return isDelete
            else:
                continue
        if(not isDelete):
            createErrorDialogBox(self,"Error","This section title doesn't exist")

   
def main():
    app = QApplication(sys.argv)
    w = BoardDetailPage()
    w.resize(640, 480)
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
