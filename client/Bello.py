import websocket
import threading
import json
import sys
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\model')
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\UI_pages')
from User import User
from Board import Board
from BelloUI import *


class Bello:
    def __init__(self):
        self.__websocket = websocket.WebSocket()
        self.__uri = "ws://localhost:8765"
        self.__user = None
        self.__ui = None

        self.__connect()

        self.receiveThread = threading.Thread(
            target=self.__handleServer, args=[])
        self.receiveThread.start()

    def __connect(self):
        self.__websocket.connect(self.__uri)
        self.__websocket.send(json.dumps({"action": "connected"}))

    def __handleMessage(self, message):
        response = message["response"]

        if response == "existedUsername":
            self.__ui.signalShowUsernameAlreadyExists.signalDict.emit(None)

        elif response == "createdAccount":
            self.__ui.gotoLoginTab()

        elif response == "loginSuccessful":
            username = self.__ui.getUsernameLogin()
            
            self.__ui.goToDashboardPage()
            self.__initUser(username)

        elif response == "loginFail":
            self.__ui.signalShowAccountDoesNotExist.signalDict.emit(None)

        elif response == "userBoardTitlesAndIds":
            boardTitlesAndIds = message["data"]

            self.__initUserBoards(boardTitlesAndIds)
            self.__ui.addBoard(boardTitlesAndIds)

        elif response == "createdBoard":
            boardDetail = message["data"]
            boardDict = {boardDetail['boardId']: boardDetail['boardTitle']}

            self.__createBoard(boardDetail)
            self.__ui.addBoard(boardDict)

        elif response == "createdSection":
            sectionDetail = message["data"]

            self.__createSection(sectionDetail)
            self.__ui.signalAddSection.signalDict.emit(sectionDetail)
            
        elif response == "createdTask":
            taskDetail = message["data"]
            print("kkk")
            self.__createTask(taskDetail)
            self.__ui.signalAddTask.signalDict.emit(taskDetail)

        elif response == "boardDetail":
            boardDetail = message["data"]

            self.__addBoardDetail(boardDetail)
            self.__ui.goToBoardDetailPage()
            self.__ui.signalInitBoardDetail.signalDict.emit(boardDetail)

        else:
            return

    def __initUser(self, username):
        self.__user = User(username)

    def __initUserBoards(self, boardTitlesAndIds):
        for boardId, boardTitle in boardTitlesAndIds.items():
            self.__user.createBoard(boardId, boardTitle)

    def __createBoard(self, boardDetail):
        boardTitle = boardDetail["boardTitle"]
        boardId = boardDetail["boardId"]

        self.__user.createBoard(boardId, boardTitle)

    def __createSection(self, sectionDetail):
        boardId = sectionDetail["boardId"]
        sectionId = sectionDetail["sectionId"]
        sectionTitle = sectionDetail["sectionTitle"]

        self.__user.createSection(boardId, sectionId, sectionTitle)
        
    def __createTask(self, taskDetail):
        boardId = taskDetail["boardId"]
        sectionId = taskDetail["sectionId"]
        taskId = taskDetail["taskId"]
        taskTitle = taskDetail["taskTitle"]
        
        self.__user.createTask(boardId, sectionId, taskId, taskTitle)

    def __addBoardDetail(self, boardDetail):
        boardId = boardDetail["boardId"]
        boardDetail = boardDetail["boardDetail"]

        self.__user.addBoardDetail(boardId, boardDetail)

    def __handleServer(self):
        while True:
            message = self.__websocket.recv()
            message = json.loads(message)

            self.__handleMessage(message)

    def editSectionTitle(self, boardId, sectionId, sectionTitle):
        self.__user.editSectionTitle(boardId, sectionId, sectionTitle)
        
        self.__websocket.send(json.dumps({"action": "editSectionTitle",
                                          "data": {
                                              "sectionId": sectionId,
                                              "sectionTitle": sectionTitle
                                          }}))
        
    def editTaskTitle(self, boardId, sectionId, taskId, taskTitle):
        self.__user.editTaskTitle(boardId, sectionId, taskId, taskTitle)
        
        self.__websocket.send(json.dumps({"action": "editTaskTitle",
                                          "data": {
                                              "taskId": taskId,
                                              "taskTitle": taskTitle
                                          }}))
        
    def signUp(self, username, password):
        self.__websocket.send(json.dumps({"action": "signUp",
                                          "data": {
                                              "username": username,
                                              "password": password}
                                          }))

    def login(self, username, password):
        self.__websocket.send(json.dumps({"action": "login",
                                          "data": {
                                              "username": username,
                                              "password": password
                                        }}))

    def validatePassword(self, password):
        return True if len(password) >= 4 else False
    
    def deleteBoard(self, boardId):
        self.__user.deleteBoard(boardId)
        
        self.__websocket.send(json.dumps({"action": "deleteBoard",
                                          "data": {
                                              "boardId": boardId
                                          }}))
        
    def deleteSection(self, boardId, sectionId):
        self.__user.deleteSection(boardId, sectionId)
        
        self.__websocket.send(json.dumps({"action": "deleteSection",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionId": sectionId
                                          }}))
        
    def deleteTask(self, boardId, sectionId, taskId):
        self.__user.deleteTask(boardId, sectionId, taskId)

        self.__websocket.send(json.dumps({"action": "deleteTask",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionId": sectionId,
                                              "taskId": taskId
                                          }}))

    def sendCreateBoardToServer(self, boardTitle):
        self.__websocket.send(json.dumps({"action": "createBoard",
                                          "data": {
                                              "boardTitle": boardTitle,
                                              "username": self.__user.getUsername()}
                                          }))

    def sendCreateSectionToServer(self, boardId, sectionTitle):
        self.__websocket.send(json.dumps({"action": "createSection",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionTitle": sectionTitle
                                          }}))
        
    def sendCreateTaskToServer(self, boardId, sectionId, taskTitle):
        print("hihihihi")
        self.__websocket.send(json.dumps({"action": "createTask",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionId": sectionId,
                                              "taskTitle": taskTitle
                                          }}))

    def sendRequestBoardDetailoServer(self, boardId):
        self.__websocket.send(json.dumps({"action": "requestBoardDetail",
                                          "data": {
                                              "boardId": boardId}
                                          }))
        
    def isExistedBoardTitle(self, boardTitle):
        boards = self.__user.getBoards()
        boardTitles = map(lambda board: board.getTitle(), boards.values())
        
        return boardTitle in boardTitles

    def addUI(self, ui):
        self.__ui = ui


if __name__ == '__main__':
    application = QApplication(sys.argv)

    bello = Bello()
    belloUI = BelloUI(None, bello)

    bello.addUI(belloUI)
    sys.exit(application.exec_())