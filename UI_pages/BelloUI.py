import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from login_signup_page import *
from dashboard_page import * 

class BelloUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setFixedSize(640,480)
        self.login_widget = Login_Signup_Page()
        self.dashboard_widget = Dashboard_Page()
        self.stack_widget = QStackedWidget()
        self.stack_widget.addWidget(self.login_widget)
        self.stack_widget.addWidget(self.dashboard_widget)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stack_widget)
        self.stack_widget.setCurrentIndex(1)
        self.setLayout(self.layout)
        
    def gotoLoginPage(self):
        self.stack_widget.setCurrentIndex(0)
    def gotoDashBoardPage(self):
        self.stack_widget.setCurrentIndex(1)
        
if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = BelloUI()
    window.show()
    sys.exit(application.exec_())