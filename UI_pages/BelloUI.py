import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginSignUpPage import *
from DashBoardPage import *
from BoardDetailPage import *
from CustomSignal import *
from SectionWidget import *

sys.path.append(
    'C:\\Users\\us\\Desktop\\Y2S2\\SEP\\project\\Bello-Task-Management\\client')

from Bello import *

class BelloUI(QMainWindow):
    def __init__(self, parent=None, bello=None):
        super(BelloUI, self).__init__(parent)
        self.bello = bello
        self.parent = parent
        self.stackedWidget = QStackedWidget()

        self.signalAddSection = CustomSignal()
        self.signalInitBoardDetail = CustomSignal()
        self.signalAddTask = CustomSignal()

        self.signalShowUsernameAlreadyExists = CustomSignal()
        self.signalShowAccountDoesNotExist = CustomSignal()

        self.loginSignUpPage = LoginSignUpPage(self)
        self.dashboardPage = DashboardPage(self)
        self.boardDetailPage = BoardDetailPage(self)

        self.signalAddSection.signalDict.connect(self.addSection)
        self.signalInitBoardDetail.signalDict.connect(self.initBoardDetail)
        self.signalAddTask.signalDict.connect(self.addTask)

        self.signalShowUsernameAlreadyExists.signalDict.connect(
            self.showUsernameAlreadyExists)
        self.signalShowAccountDoesNotExist.signalDict.connect(
            self.showAccountDoesNotExist)

        self.stackedWidget.addWidget(self.loginSignUpPage)
        self.stackedWidget.addWidget(self.dashboardPage)
        self.stackedWidget.addWidget(self.boardDetailPage)
        self.stackedWidget.setCurrentIndex(0)

        self.loginSignUpPage.loginWidget.loginBtn.clicked.connect(
            self.__loginAccount)
        self.loginSignUpPage.signUpWidget.signUpBtn.clicked.connect(
            self.__signUpAccount)
        self.dashboardPage.createBtn.clicked.connect(self.__createBoard)
        self.dashboardPage.displayBoard.listWidget.itemDoubleClicked.connect(
            self.__requestBoardDetail)
        self.dashboardPage.deleteBoardBtn.clicked.connect(self.__deleteBoard)
        self.boardDetailPage.dialogCreate.button.clicked.connect(
            self.__createSection)
        self.boardDetailPage.menuBar.homeBtn.clicked.connect(self.__homeBtnFunc)
        
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
      
        if (not self.dashboardPage.validateBoardTitle()) or self.showBoardTitleIsExist(boardTitle):
            return

        self.bello.sendCreateBoardToServer(boardTitle)
        self.dashboardPage.closeDialog()

    def __createSection(self):
        if not self.boardDetailPage.validateSectionTitle():
            return

        boardId = self.boardDetailPage.getBoardId()
        sectionTitle = self.boardDetailPage.getSectionNameFromDialog()

        self.boardDetailPage.closeCreateNewSectionDialog()
        self.bello.sendCreateSectionToServer(boardId, sectionTitle)

    def createTask(self,boardId, sectionId, taskTitle,taskOrder):
        self.bello.sendCreateTaskToServer(boardId, sectionId, taskTitle,taskOrder)

    def __requestBoardDetail(self):
        boardId = self.getSelectedBoard()

        self.bello.sendRequestBoardDetailToServer(boardId)

    def __deleteBoard(self):
        boardId = self.dashboardPage.deleteSelectBoard()

        self.bello.deleteBoard(boardId)
    
    def __homeBtnFunc(self):
        self.boardDetailPage.clearAllSection()
        self.goToDashboardPage()
        
    def deleteSection(self, boardId, sectionId):
        self.bello.deleteSection(boardId, sectionId)
        
    def deleteTask(self, boardId, sectionId, taskId):
        self.bello.deleteTask(boardId, sectionId, taskId)

    def addBoard(self, boardDict):
        self.dashboardPage.addBoard(boardDict)

    def addSection(self, sectionDict):
        self.boardDetailPage.createSection(sectionDict)
    
    def addTask(self,taskDict):
        self.boardDetailPage.createNewTask(taskDict)
        
    def addTaskComment(self, boardId, sectionId, taskId, taskComment):
        #TODO
        self.bello.addTaskComment(boardId, sectionId, taskId, taskComment)
        
    def addTaskTag(self, boardId, sectionId, taskId, taskTag):
        #TODO
        self.bello.addTaskTag(boardId, sectionId, taskId, taskTag)

    def editSectionTitle(self, sectionId, sectionTitle):
        boardId = self.boardDetailPage.getBoardId()

        self.bello.editSectionTitle(boardId, sectionId, sectionTitle)
        
    def editTaskTitle(self, sectionId, taskId, taskTitle):
        boardId = self.boardDetailPage.getBoardId()
        
        self.bello.editTaskTitle(boardId, sectionId, taskId, taskTitle)
        
    def reorderTaskInSameSection(self, boardId, sectionId, taskId, taskOrder):
        self.bello.reorderTaskInSameSection(boardId, sectionId, taskId, taskOrder)
        
    def reorderTaskInDifferentSection(self, boardId, sectionId, newSectionId, taskId, taskOrder):
        self.bello.reorderTaskInDifferentSection(boardId, sectionId, newSectionId, taskId, taskOrder)

    def initBoardDetail(self, boardDetailDict):
        self.boardDetailPage.initBoardDetail(boardDetailDict)

    def getUsernameLogin(self):
        return self.loginSignUpPage.loginWidget.usernameValueLogin.text()

    def getBoardName(self):
        self.dashboardPage.getBoardName()

    def getSelectedBoard(self):
        return self.dashboardPage.displayBoard.getSelectItemInBoardId()

    def setSectionId(self, sectionId):
        self.boardDetailPage.sectionWidget.setSectionId(sectionId)
        
    def setTaskDueDate(self, boardId, sectionId, taskId, taskDueDate):
        self.bello.setTaskDueDate(boardId, sectionId, taskId, taskDueDate)

    def setTaskFinishState(self, taskId, taskState):
        print("taskid: ",taskId)
        print("taskState: ", taskState)
        self.bello.setTaskFinishState(taskId, taskState)
        print("finish")
    
    def showUsernameAlreadyExists(self):
        self.loginSignUpPage.signUpWidget.showUsernameAlreadyExistsSignUp()

    def showAccountDoesNotExist(self):
        self.loginSignUpPage.loginWidget.showLoginError()

    def showBoardTitleIsExist(self,boardTitle):
        for i in range(self.dashboardPage.displayBoard.listWidget.count()):
            if(self.dashboardPage.displayBoard.listWidget.item(i).text() == boardTitle):
                self.dashboardPage.showBoardTitleIsExist()
                return True    
        return False

    def gotoLoginTab(self):
        self.loginSignUpPage.tabWidget.setCurrentIndex(0)

    def goToLoginSignUpPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToDashboardPage(self):
        username = self.getUsernameLogin()
        self.dashboardPage.menuBar.setFirstChaOfUsername(username)
        self.stackedWidget.setCurrentIndex(1)

    def goToBoardDetailPage(self):
        username = self.getUsernameLogin()
        self.boardDetailPage.menuBar.setFirstChaOfUsername(username)
        if self.getSelectedBoard() == None:
            return

        self.boardDetailPage.setBoardId(self.getSelectedBoard())
        self.stackedWidget.setCurrentIndex(2)