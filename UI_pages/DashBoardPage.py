import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint
from TabBar import * 
from MenuBar import * 

class TextOverDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(TextOverDelegate, self).__init__(parent)
    def paint(self, painter, option, index):
        super(TextOverDelegate,self).paint(painter,option,index)
        text = index.data(QtCore.Qt.UserRole)
        if(option.widget):
            style = option.widget.style()
        else:
            style = QApplication.style()
        style.drawItemText(painter, option.rect,QtCore.Qt.AlignCenter, option.palette, option.state & QStyle.State_Enabled, text)

class DisplayBoardBox(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setFixedSize(480,350)
        self.listWidget = QListWidget()
        self.listWidget.setSpacing(10)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listWidget)
        self.listWidget.setIconSize(QSize(200,80))
        self.listWidget.setFont(QFont("Moon",10))
        self.setLayout(self.layout)
        self.i = 1
    def createBox(self,text):
        self.ran_num1 = randint(0,150)
        self.ran_num2 = randint(0,199)
        self.ran_num3 = randint(0,226)
        self.board1 = QListWidgetItem()
        self.board1.setBackground(QColor(self.ran_num1,self.ran_num2,self.ran_num3))
        self.board1.setSizeHint(QSize(120, 80))
        self.board1.setFont(QFont("Century Gothic", 12, QFont.Bold))
        self.board1.setTextColor("white")
        self.board1.setTextAlignment(Qt.AlignLeft)
        self.board1.setText(text)
        self.addToListWidget(self.board1)
    def addToListWidget(self,board):
        self.i += 1 
        self.listWidget.insertItem(self.i,board)

class DashboardPage(QWidget):
    def __init__(self,parent=None):
        super(DashboardPage,self).__init__(parent)
        self.parent = parent
        self.menuBar = MenuBar()
        self.menuBar.move(QPoint(0,0))
        self.tabBarBoard = TabWidget()
        self.tabBarBoard.setFixedSize(585,355)
        self.tabBarBoard.setFont(QFont("Moon",10,QFont.Bold))
        self.displayBoard = DisplayBoardBox()
        self.addBoardBtn = QPushButton("Add")
        self.addBoardBtn.setIcon(QIcon("images/add.png"))
        self.addBoardBtn.setStyleSheet("background-color:rgb(14,172,120);color:rgb(255,255,255)")
        self.addBoardBtn.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.addBoardBtn.clicked.connect(self.createNewBoard)
        self.deleteBoardBtn = QPushButton("Delete")
        self.deleteBoardBtn.setIcon(QIcon("images/delete.png"))
        self.deleteBoardBtn.setStyleSheet("background-color:rgb(210,39,62);color:rgb(255,255,255)")
        self.deleteBoardBtn.setFont(QFont("Century Gothic",8,QFont.Bold))
        self.deleteBoardBtn.clicked.connect(self.deleteSelectBoard)
        self.tabBarBoard.addTab(self.displayBoard, QIcon("images/boardIcon.png"), " Board")
        self.layout = QGridLayout()
        self.menuBar.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.menuBar, 0,0 )
        #self.layout.addLayout(self.menubar_widget,0,0)
        self.tabBarBoard.setContentsMargins(10,0,30,0)
        self.layout.addWidget(self.tabBarBoard,1,0,1,2)
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addStretch(1)
        self.btnLayout.addWidget(self.addBoardBtn)
        self.btnLayout.addWidget(self.deleteBoardBtn)
        self.layout.addLayout(self.btnLayout,2,0)
        self.setLayout(self.layout)
        self.show()
    
    def createNewBoard(self):
        self.createBoardDialog = QDialog(self)
        self.createBoardDialog.setWindowTitle("Create board")
        self.formLayout = QFormLayout()
        self.boardNameLabel = QLabel("Board Name: ")
        self.boardNameValue = QLineEdit(self)
        self.createBtn = QPushButton('Create')
        self.formLayout.addRow(self.boardNameLabel,self.boardNameValue)
        self.formLayout.addRow(self.createBtn)
        self.createBoardDialog.setLayout(self.formLayout)
        self.boardNameLabel.setFont(QFont("Century Gothic", 10))
        self.boardNameValue.setFont(QFont("Century Gothic",10))
        self.createBtn.setFont(QFont("Moon",10))
        self.createBtn.clicked.connect(self.createBtnAddBoard)
        self.createBoardDialog.show()

    def getBoardName(self):
        return self.boardNameValue.text()
    def addBoard(self,boardName):
        self.board = QListWidgetItem(QIcon(self.displayBoard.createBox()), boardName)
        self.displayBoard.addToListWidget(self.board)
        
    def createBtnAddBoard(self):
        boardName = self.getBoardName()
        self.displayBoard.createBox(boardName)
        self.displayBoard.setContentsMargins(10,10,10,10)
        self.closeDialog()
    def closeDialog(self):
        self.createBoardDialog.reject()
    def deleteSelectBoard(self):
        print("delete")
        self.select_board = self.displayBoard.listWidget.selectedItems()
        if not self.select_board:
            return
        for item in self.select_board:
            self.displayBoard.listWidget.takeItem(self.displayBoard.listWidget.row(item))
def main():
    app = QApplication(sys.argv)
    w = DashboardPage()
    w.resize(640, 480)
    w.show()
    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())