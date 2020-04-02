import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginSignUpPage import *
from DashboardPage import * 

class BelloUI(QMainWindow):
    def __init__(self,parent = None):
        super(BelloUI,self).__init__(parent)
        self.parent = parent
        self.stackedWidget = QStackedWidget()
        self.loginSignUpPage = LoginSignUpPage(self)
        self.dashboardPage = DashboardPage(self)
        self.stackedWidget.addWidget(self.loginSignUpPage)
        self.stackedWidget.addWidget(self.dashboardPage)
        self.stackedWidget.setCurrentIndex(0)
        self.loginSignUpPage.loginWidget.loginBtn.clicked.connect(self.gotoDashboardPage)
        self.setCentralWidget(self.stackedWidget)
        self.setFixedSize(640,480)
        self.show()
    def getUsernameLogin(self):
        return self.loginSignUpPage.loginWidget.usernameValueLogin.text()
    def getPasswordLogin(self):
        return self.loginSignUpPage.loginWidget.passwordValueLogin.text()
    def getUsernameSignUp(self):
        return self.loginSignUpPage.signupWidget.usernameValueSignUp.text()
    def getPasswordSignUp(self):
        return self.loginSignUpPage.signupWidget.passwordValueSignUp.text()
    def getBoardName(self):
        self.dashboardPage.getBoardName()
    def getConfirmPassword(self):
        return self.loginSignUpPage.signupWidget.confirmPasswordValue.text()
    def gotoLoginSignUpPage(self):
        self.stackedWidget.setCurrentIndex(0)
    def gotoDashboardPage(self):
        self.stackedWidget.setCurrentIndex(1)
    def addBoard(self):
        self.dashboardPage.addBoard()
    def deleteBoard(self):
        self.dashboardPage.deleteSelectBoard()
if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = BelloUI()
    sys.exit(application.exec_())