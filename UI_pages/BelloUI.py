import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginSignUpPage import *
from DashboardPage import *
from BoardDetailPage import *

sys.path.append(
    'C:\\Users\\us\\Desktop\\Y2S2\\SEP\\project\\Bello-Task-Management\\client')
from Bello import *

class BelloUI(QMainWindow):
    def __init__(self, parent=None, bello=None):
        super(BelloUI, self).__init__(parent)
        self.bello = bello
        self.parent = parent
        self.stackedWidget = QStackedWidget()
        self.loginSignUpPage = LoginSignUpPage(self)
        self.dashboardPage = DashboardPage(self)
        self.boardDetailPage = BoardDetailPage(self)
        self.stackedWidget.addWidget(self.loginSignUpPage)
        self.stackedWidget.addWidget(self.dashboardPage)
        self.stackedWidget.addWidget(self.boardDetailPage)
        self.stackedWidget.setCurrentIndex(0)
        self.loginSignUpPage.loginWidget.loginBtn.clicked.connect(
            self.__loginAccount)
        self.loginSignUpPage.signUpWidget.signUpBtn.clicked.connect(
            self.__signUpAccount)
        self.dashboardPage.createBtn.clicked.connect(self.__createBoard)
        self.dashboardPage.displayBoard.listWidget.itemSelectionChanged.connect(self.getSelectedBoard) #return the boardID of sekected board

        #self.boardDetailPage.newSectionWidget[2].clicked.connect(self.__createSection) #createSection in BoardDetail
         
        self.dashboardPage.menuBar.homeBtn.clicked.connect(self.goToDashboardPage)
        self.setCentralWidget(self.stackedWidget)
        self.setFixedSize(640, 480)
        
        self.show()

    def __loginAccount(self):
        username = self.getUsernameLogin()
        password = self.__getPasswordLogin()

        self.bello.login(username, password)
    
    def __validateSignUpPassword(self, password):
        confirmPassword = self.__getConfirmPassword()

        if password != confirmPassword:
            self.__showConfirmPasswordMismatch()
            return False

        elif not self.bello.validatePassword(password):
            self.__showInvalidPasswordLength()
            return False

        return True

    def __getPasswordLogin(self):
        return self.loginSignUpPage.loginWidget.passwordValueLogin.text()

    def __getUsernameSignUp(self):
        return self.loginSignUpPage.signUpWidget.usernameValueSignUp.text()

    def __getPasswordSignUp(self):
        return self.loginSignUpPage.signUpWidget.passwordValueSignUp.text()

    def __getConfirmPassword(self):
        return self.loginSignUpPage.signUpWidget.confirmPasswordValue.text()

    def __showConfirmPasswordMismatch(self):
        self.loginSignUpPage.signUpWidget.showComfirmPasswordMismatch()

    def __showInvalidPasswordLength(self):
        self.loginSignUpPage.signUpWidget.showInvalidPasswordLength()

    def __signUpAccount(self):
        username = self.__getUsernameSignUp()
        password = self.__getPasswordSignUp()

        if not self.__validateSignUpPassword(password):
            return

        self.bello.signUp(username, password)
        
    def __createBoard(self):
        boardTitle = self.dashboardPage.getBoardTitle()
         
        if not self.dashboardPage.validateBoardTitle() or self.bello.isExistedBoardTitle(boardTitle):
            return
        
        self.bello.sendCreateBoardToServer(boardTitle)
        self.dashboardPage.closeDialog()
        
    def __createSection(self):
        if(not self.boardDetailPage.validateSectionTitle()):
            return
        boardId = self.boardDetailPage.getBoardId()
        sectionTitle = self.boardDetailPage.getSectionNameFromDialog()
        self.bello.sendCreateSectionToServer(boardId, sectionTitle) 
        
    def __editSectionTitle(self):
        boardId = self.boardDetailPage.getBoardId()
        sectionId = self.boardDetailPage.sectionWidget.getSectionId()
        sectionTitle = self.boardDetailPage.sectionWidget.getSectionTitle()
        self.bello.editSectionTitle(boardId, sectionId, sectionTitle)
        self.bello.sendEditSectionTitleToServer(sectionId, sectionTitle)
        self.boardDetailPage.sectionWidget.editTitle(sectionTitle)

    def addBoard(self, boardDict):
        self.dashboardPage.addBoard(boardDict)
        
    def addSection(self,sectionDict):
        self.boardDetailPage.createSection(sectionDict)
    
    def getUsernameLogin(self):
        return self.loginSignUpPage.loginWidget.usernameValueLogin.text()

    def getBoardName(self):
        self.dashboardPage.getBoardName()

    def getSelectedBoard(self):
        self.dashboardPage.displayBoard.getSelectItemInBoardID() #return in boardID

    def setSectionId(self, sectionId):
        self.boardDetailPage.sectionWidget.setSectionId(sectionId)

    def showUsernameAlreadyExists(self):
        self.loginSignUpPage.signUpWidget.showUsernameAlreadyExistsSignUp()
    
    def showAccountDoesNotExist(self):
        self.loginSignUpPage.loginWidget.showLoginError()
    
    def clearErrorMessageLogin(self):
        self.loginSignUpPage.loginWidget.clearTextErrorLogin()

    def clearErrorMessageSignUp(self):
        self.loginSignUpPage.signUpWidget.clearTextErrorSignUp()

    def gotoLoginTab(self):
        self.loginSignUpPage.tabWidget.setCurrentIndex(0)

    def goToLoginSignUpPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToDashboardPage(self):
        username = self.getUsernameLogin()
        self.dashboardPage.menuBar.setFirstChaOfUsername(username)
        self.stackedWidget.setCurrentIndex(1)

    def goToBoardDetailPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def addBoard(self, boardDict):
        self.dashboardPage.addBoard(boardDict)
        self.dashboardPage.closeDialog()
        
    def initBoard(self, boardDict):
        self.dashboardPage.addBoard(boardDict)
    
    def initBoardDetial(self,boardDetailDict):
        self.dashboardPage.initBoardDetial(boardDetailDict)

    def createNewSection(self):
        self.boardDetailPage.setBoardId(self.getSelectedBoard())
        self.boardDetailPage.createNewSection()

    def closeDialogBoxInCreateSection(self):
        self.boardDetailPage.closeDialogBox()

    def deleteBoard(self):
        self.dashboardPage.deleteSelectBoard()

