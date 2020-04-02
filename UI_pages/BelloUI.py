import sys
import asyncio
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginSignUpPage import *
from DashboardPage import *
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\client')
from Bello import *


class BelloUI(QMainWindow):
    def __init__(self, parent=None, bello=None):
        super(BelloUI, self).__init__(parent)
        
        self.bello = bello
        
        self.parent = parent
        self.stackedWidget = QStackedWidget()
        self.loginSignUpPage = LoginSignUpPage(self)
        self.dashboardPage = DashboardPage(self)
        self.stackedWidget.addWidget(self.loginSignUpPage)
        self.stackedWidget.addWidget(self.dashboardPage)
        self.stackedWidget.setCurrentIndex(0)
        self.loginSignUpPage.loginWidget.loginBtn.clicked.connect(
            self.goToDashboardPage)
        self.setCentralWidget(self.stackedWidget)
        self.setFixedSize(640, 480)
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

    def goToLoginSignUpPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToDashboardPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def addBoard(self, boardName):
        self.dashboardPage.addBoard(boardName)

    def deleteBoard(self):
        self.dashboardPage.deleteSelectBoard()


# if __name__ == '__main__':
#     application = QApplication(sys.argv)
#     window = BelloUI()
#     sys.exit(application.exec_())
