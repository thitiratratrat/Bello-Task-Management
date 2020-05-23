import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from LoginSignUpPage import *
from DashBoardPage import *
from BoardDetailPage import *
from CustomSignal import *
from SectionWidget import *
from dialogBox import *

sys.path.append(
    sys.path[0] + "\\..\\client")

path = sys.path[0] + "\\..\\images" 

from Bello import *

class BelloUI(QMainWindow):
    def __init__(self, parent=None, bello=None):
        super(BelloUI, self).__init__(parent)
        self.bello = bello
        self.parent = parent
        self.path = path
        self.stackedWidget = QStackedWidget()
        self.setWindowTitle("Bello")
        self.signalAddSection = CustomSignal()
        self.signalInitBoardDetail = CustomSignal()
        self.signalAddTask = CustomSignal()
        self.signalDeleteBoard = CustomSignal()

        self.signalShowUsernameAlreadyExists = CustomSignal()
        self.signalShowAccountDoesNotExist = CustomSignal()
        self.signalShowMemberUsernameDoesNotExists = CustomSignal()
        self.signalAddMemberInMenuBar = CustomSignal()
        self.signalDeleteBoardDialog =CustomSignal()
        self.signalUpdateBoard = CustomSignal()

        self.loginSignUpPage = LoginSignUpPage(self)
        self.dashboardPage = DashboardPage(self)
        self.boardDetailPage = BoardDetailPage(self)

        self.signalAddSection.signalDict.connect(self.addSection)
        self.signalInitBoardDetail.signalDict.connect(self.initBoardDetail)

        self.signalUpdateBoard.signalDict.connect(self.initUpdateBoardDetail)
        self.signalDeleteBoard.signalDict.connect(self.showDeletedDialog)
        self.signalAddTask.signalDict.connect(self.addTask)
        self.signalAddMemberInMenuBar.signalDict.connect(self.addMember)

        self.signalShowUsernameAlreadyExists.signalDict.connect(
            self.showUsernameAlreadyExists)
        self.signalShowAccountDoesNotExist.signalDict.connect(
            self.showAccountDoesNotExist)

        self.signalDeleteBoardDialog.signalDict.connect(self.showDeletedBoardDialog)

        self.signalShowMemberUsernameDoesNotExists.signalDict.connect(
            self.boardDetailPage.showMemberDoesNotExists)

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

        username = self.getUsernameLogin()
        self.bello.sendCreateBoardToServer(boardTitle, username)
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
        self.boardDetailPage.menuBar.memberColor = ["#2E8B57", "#4682B4", "#B22222","#008080","#31446F"]
        self.goToDashboardPage()
        
    def deleteSection(self, boardId, sectionId):
        self.bello.deleteSection(boardId, sectionId)
    
    def deleteTask(self, sectionId, taskId):
        self.bello.deleteTask(sectionId, taskId)
        
    def deleteTaskComment(self, taskId, taskCommentOrder):
        self.bello.deleteTaskComment(taskId, taskCommentOrder)
        
    def deleteTaskTag(self, taskId, taskTag):
        self.bello.deleteTaskTag(taskId, taskTag)

    def addBoard(self, boardDict):
        self.dashboardPage.addBoard(boardDict)

    def addBoardUpdate(self,boardDict):
        self.dashboardPage.deleteAllBoard()
        self.dashboardPage.addBoard(boardDict)

    def addSection(self, sectionDict):
        self.boardDetailPage.createSection(sectionDict)
    
    def addTask(self,taskDict):
        self.boardDetailPage.createNewTask(taskDict)
      
    def addTaskComment(self, taskId, taskComment, memberUsername, taskCommentOrder):
        self.bello.addTaskComment(taskId, taskComment, memberUsername, taskCommentOrder)
      
    def addTaskTag(self, taskId, taskTag, taskTagColor):
        self.bello.addTaskTag(taskId, taskTag, taskTagColor)

    def addMember(self ):
        memberUsername  = self.boardDetailPage.addMemberDialog.lineEdit.text()
        self.boardDetailPage.addMember(memberUsername)
        self.boardDetailPage.addMemberInCombo(memberUsername)

    def addMemberToBoard(self,boardId,memberUsername):
        self.bello.addMemberToBoard(boardId, memberUsername)
        
    def setTaskResponsibleMember(self, taskId, memberUsername):
        self.bello.setTaskResponsibleMember(taskId, memberUsername)

    def editSectionTitle(self, sectionId, sectionTitle):
        self.bello.editSectionTitle(sectionId, sectionTitle)
    
    def editTaskTitle(self, taskId, taskTitle):
        self.bello.editTaskTitle(taskId, taskTitle)
    
    def reorderTaskInSameSection(self, sectionId, taskId, taskOrder):
        self.bello.reorderTaskInSameSection(sectionId, taskId, taskOrder)
        
    def reorderTaskInDifferentSection(self, sectionId, newSectionId, taskId, taskOrder):
        self.bello.reorderTaskInDifferentSection(sectionId, newSectionId, taskId, taskOrder)

    def initBoardDetail(self, boardDetailDict):
        self.boardDetailPage.initBoardDetail(boardDetailDict)

    def initUpdateBoardDetail(self, boardDetailDict):
        self.boardDetailPage.menuBar.memberColor = ["#2E8B57", "#4682B4", "#B22222","#008080","#31446F"]
        self.boardDetailPage.initBoardDetail(boardDetailDict)

    def getUsernameLogin(self):
        return self.loginSignUpPage.loginWidget.usernameValueLogin.text()

    def getBoardName(self):
        self.dashboardPage.getBoardName()

    def getSelectedBoard(self):
        return self.dashboardPage.displayBoard.getSelectItemInBoardId()

    def setSectionId(self, sectionId):
        self.boardDetailPage.sectionWidget.setSectionId(sectionId)
        
    def setTaskDueDate(self, taskId, taskDueDate):
        self.bello.setTaskDueDate(taskId, taskDueDate)

    def setTaskFinishState(self, taskId, taskState):
        self.bello.setTaskFinishState(taskId, taskState)
    
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

    def showDeletedBoardDialog(self,deletedBoardId): 
        createErrorDialogBox(self,"Board is Deleted","Board has been deleted")
        self.dashboardPage.deleteBoardId(deletedBoardId)
        self.goToDashboardPage()
    
    def showDeletedDialog(self,deletedBoardId):
        createErrorDialogBox(self,"Board is Deleted","Board has been deleted")
        self.dashboardPage.deleteBoardId(deletedBoardId)

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
       
        self.boardDetailPage.menuBar.setBoardTitle("  Board title: "+ 
            self.dashboardPage.displayBoard.getBoardTitle() + "  ")
        if self.getSelectedBoard() == None:
            return

        self.boardDetailPage.setBoardId(self.getSelectedBoard())
        self.stackedWidget.setCurrentIndex(2)