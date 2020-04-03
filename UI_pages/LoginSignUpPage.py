import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginWidget import * 
from SignUpWidget import * 

class LoginSignUpPage(QWidget):
    def __init__(self,parent):
        super(LoginSignUpPage,self).__init__(parent)
        self.parent = parent
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("color: rgb(82,113,159)")
        self.loginWidget= LoginWidget()
        self.tabWidget.setFixedSize(313,263)
        self.signUpWidget = SignUpWidget()
        self.tabWidget.setFont(QFont("Century Gothic", 9 ,QFont.Bold))
        self.tabWidget.addTab(self.loginWidget, "Log in")
        self.tabWidget.addTab(self.signUpWidget, "Sign up")
        self.setWindowTitle("Bello project")
        self.belloLabel = QLabel("Bello")
        self.loginSignUpLayout = QVBoxLayout()
        self.setContentsMargins(150,60,20,140)
        self.belloLabel.setContentsMargins(133,0,0,25)
        self.loginSignUpLayout.addWidget(self.belloLabel)
        self.loginSignUpLayout.addWidget(self.tabWidget)
        self.belloLabel.setFont(QFont("Moon", 24,QFont.Bold))
        self.setLayout(self.loginSignUpLayout)
        self.belloIcon = QPixmap("images/iconBello.png")
        self.show()
    def paintEvent(self,e):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(248,215,60))
        paint.setBrush(QColor(248,215,60))
        paint.drawEllipse(QPoint(20,350), 125, 125)
        paint.drawEllipse(QPoint(620,140), 125, 125)
        paint.setPen(QColor(255,160,122))
        paint.setBrush(QColor(255,160,122))
        paint.drawPolygon([QPoint( 60,60),QPoint(140,110),QPoint(130,200)])
        paint.drawPolygon([QPoint(350,430),QPoint(540,300),QPoint(570,390),])
        paint.drawPixmap(QRect(245,60,40,40),self.belloIcon)
        paint.end()