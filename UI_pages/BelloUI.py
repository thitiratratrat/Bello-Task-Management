import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginSignUpPage import *
from DashBoardPage import * 

class BelloUI(QMainWindow):
    def __init__(self,parent = None):
        super(BelloUI,self).__init__(parent)
        self.parent = parent
        self.setFixedSize(640,480)
        self.initialPage()
        self.show()
    def initialPage(self):
        self.login_widget = Login_Signup_Page(self)
        self.layout = QVBoxLayout()
        self.login_widget.setLayout(self.layout)
        self.setCentralWidget(self.login_widget)

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = BelloUI()
    sys.exit(application.exec_())