import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from random import randint

class TabBar(QTabBar):
     def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s
     def paintEvent(self, event):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()
        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()
            s = opt.rect.size()
            s.transpose()
            r = QRect(QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r
            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt);
            painter.restore()
class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.tabBar = TabBar(self)
        self.tabBar.tabSizeHint(0)
        self.setTabBar(self.tabBar)
        self.setTabPosition(QTabWidget.West)

class MenuBar(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        #self.setFixedSize(640,20)
        #self.setColor()
        # self.setContentsMargins(0,-5,30,0)
        self.setContentsMargins(0,0,0,0)
        self.homeBtn = QPushButton("Home")
        self.homeBtn.setIcon(QIcon('images/homeIcon.png'))
        self.homeBtn.setStyleSheet("background-color: rgb(87,85,85); color: white")
        self.homeBtn.setFont(QFont("Century Gothic",8))
        self.boardBtn = QPushButton("Board")
        self.boardBtn.setIcon(QIcon('images/boardIcon.png'))
        self.boardBtn.setStyleSheet("background-color: rgb(87,85,85); color: white")
        self.boardBtn.setFont(QFont("Century Gothic",8))
        self.menubar_widget = QHBoxLayout()
        self.menubar_widget.addWidget(self.homeBtn)
        self.menubar_widget.addWidget(self.boardBtn)
        self.menubar_widget.addStretch(1)
        self.setLayout(self.menubar_widget)

class DisplayBoardBox(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.list_widget = QListWidget()
        self.list_widget.setViewMode(QListWidget.IconMode)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.list_widget)
        self.list_widget.setIconSize(QSize(200,80))
        self.list_widget.setFont(QFont("Moon",10))
        self.board1 = QListWidgetItem(QIcon(self.createBox()),"Bello")
        self.list_widget.insertItem(1,self.board1)
        self.setLayout(self.layout)
        self.i = 1
    def createBox(self):
        self.ran_num1 = randint(0,255)
        self.ran_num2 = randint(0,255)
        self.ran_num3 = randint(0,255)
        self.recPainter = QPixmap(120, 80)
        self.recPainter.fill(QColor(self.ran_num1,self.ran_num2,self.ran_num3))
        return self.recPainter
    def addto_list_widget(self,board):
        self.i += 1 
        self.list_widget.insertItem(self.i,board)

class Dashboard_Page(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.menuBar = MenuBar()
        self.tabBarBoard = TabWidget()
        self.tabBarBoard.setFont(QFont("Moon",10,QFont.Bold))
        self.display_board = DisplayBoardBox()
        self.add_board_btn = QPushButton("+ ADD board")
        self.add_board_btn.clicked.connect(self.create_new_board)
        self.delete_board_btn = QPushButton("- Delete board")
        self.delete_board_btn.clicked.connect(self.delete_selected_board)
        self.tabBarBoard.addTab(self.display_board, QIcon("images/boardIcon.png"), " Board")
        self.tabBarBoard.addTab(QWidget(),"Team")
        self.layout = QGridLayout()
        self.menuBar.setContentsMargins(0,0,0,20)
        self.layout.addWidget(self.menuBar,0,0)
        self.tabBarBoard.setContentsMargins(10,0,30,0)
        self.layout.addWidget(self.tabBarBoard,1,0,1,2)
        self.layout.addWidget(self.add_board_btn,2,1,1,2)
        self.layout.addWidget(self.delete_board_btn,2,2,1,2)
        self.setLayout(self.layout)
    def paintEvent(self,e):
        paint = QPainter()
        paint.begin(self)
        '''paint.setPen(QColor(255,219,128))
        paint.setBrush(QColor(255,219,128))
        paint.drawEllipse(QPoint(20,350), 125, 125)
        paint.drawEllipse(QPoint(620,140), 125, 125)'''
        paint.setPen(QColor(61,59,59))
        paint.setBrush(QColor(61,59,59))
        paint.drawRect(0,0, 640, 48)
        paint.end()
    def create_new_board(self):
        self.create_board = QDialog(self)
        self.create_board.setWindowTitle("Create board")
        self.formLayout = QFormLayout()
        self.bName_label = QLabel("Board Name: ")
        self.b_name_lineEdit = QLineEdit(self)
        self.create_btn = QPushButton('Create')
        self.create_btn.clicked.connect(self.add_board)
        self.formLayout.addRow(self.bName_label,self.b_name_lineEdit)
        self.formLayout.addRow(self.create_btn)
        self.create_board.setLayout(self.formLayout)
        self.bName_label.setFont(QFont("Century Gothic", 10))
        self.b_name_lineEdit.setFont(QFont("Century Gothic",10))
        self.create_btn.setFont(QFont("Moon",10))
        self.create_board.show()
    def add_board(self):
        b_name = self.b_name_lineEdit.text()
        self.board = QListWidgetItem(QIcon(self.display_board.createBox()), b_name)
        self.display_board.addto_list_widget(self.board)
        self.create_board.reject()
    def delete_selected_board(self):
        print("delete")
        self.select_board = self.display_board.list_widget.selectedItems()
        if not self.select_board:
            return
        for item in self.select_board:
            self.display_board.list_widget.takeItem(self.display_board.list_widget.row(item))
def main():
    app = QApplication(sys.argv)
    w = Dashboard_Page()
    w.resize(640, 480)
    w.show()
    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())