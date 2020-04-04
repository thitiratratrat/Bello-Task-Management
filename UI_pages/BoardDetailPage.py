import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MenuBar import *

class TaskWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

class Section(QListWidget): #addtask is here
    def __init__(self):
        QListWidget.__init__(self,None)
        self.setFixedSize(200,480)

class SectionWidget(QWidget):
    def __init__(self,parent=None):
        super(SectionWidget,self).__init__(None)
        self.section = Section()
        self.mainSectionLayout = QVBoxLayout()
        self.label = QLabel("Sectioname")
        self.mainSectionLayout.addWidget(self.label)
        self.mainSectionLayout.addWidget(self.section)
        #self.mainSectionLayout.addWidget(self.label)
        #self.mainSectionLayout.addLayout(self.sectionLayout)
        self.setLayout(self.mainSectionLayout)
        
class BoardDetailPage(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.menuBar = MenuBar()

        self.sectionLayout = QHBoxLayout()
        self.widget = QWidget()
        for i in range(10):
            self.sectionWidget = SectionWidget()
            self.sectionLayout.addWidget(self.sectionWidget)
        self.widget.setLayout(self.sectionLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

        self.boardDetailLayout = QVBoxLayout()
        self.boardDetailLayout.addWidget(self.menuBar)
        self.boardDetailLayout.addWidget(self.scrollArea)
        self.setLayout(self.boardDetailLayout)

def main():
    app = QApplication(sys.argv)
    w = BoardDetailPage()
    w.resize(640, 480)
    w.show()
    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())
