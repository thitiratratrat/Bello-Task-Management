import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginWidget import * 
from SignUpWidget import * 
from BelloUI import *

class Login_Signup_Page(QWidget):
    def __init__(self,parent):
        #QWidget.__init__(self,None)
        super(Login_Signup_Page,self).__init__(parent)
        self.parent = parent
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("color: rgb(82,113,159)")
        self.login= LoginWidget(self)
        self.tabWidget.setFixedSize(313,263)
        self.signup = SignUpWidget()
        self.tabWidget.setFont(QFont("Century Gothic", 9 ,QFont.Bold))
        self.tabWidget.addTab(self.login, "Log in")
        self.tabWidget.addTab(self.signup, "Sign up")
        self.setWindowTitle("Bello project")
        self.project_name_label = QLabel("Bello")
        self.login_signup_layout = QVBoxLayout()
        self.setContentsMargins(150,60,20,140)
        self.project_name_label.setContentsMargins(133,0,0,25)
        self.login_signup_layout.addWidget(self.project_name_label)
        self.login_signup_layout.addWidget(self.tabWidget)
        self.project_name_label.setFont(QFont("Moon", 24,QFont.Bold))
        self.setLayout(self.login_signup_layout)
        self.icon_Bello = QPixmap("images/iconBello.png")
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
        paint.drawPixmap(QRect(245,60,40,40),self.icon_Bello)
        paint.end()
    def changetoDashPage(self):
        self.dashboard_widget = Dashboard_Page(self.parent)
        self.layout = QVBoxLayout()
        self.dashboard_widget.setLayout(self.layout)
        self.parent.setCentralWidget(self.dashboard_widget)
def main():
    app = QApplication(sys.argv)
    w = Login_Signup_Page(BelloUI())
    w.setFixedSize(640, 480)
    
    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())