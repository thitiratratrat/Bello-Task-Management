import websocket
import threading
import json
import sys
sys.path.append(
    'C:\\Users\\us\\Desktop\\Y2S2\\SEP\\project\\Bello-Task-Management\\model')
sys.path.append(
    'C:\\Users\\us\\Desktop\\Y2S2\\SEP\\project\\Bello-Task-Management\\UI_pages')
from BelloUI import *
from User import User
from Board import Board
from dialogBox import * 


class Bello:
    def __init__(self):
        super(Bello, self).__init__()
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
            self.__ui.showUsernameAlreadyExists()

        elif response == "createdAccount":
            self.__ui.gotoLoginTab()

        elif response == "loginSuccessful":
            username = self.__ui.getUsernameLogin()
            self.__ui.goToDashboardPage()
            self.__initUser(username)

        elif response == "loginFail":
            self.__ui.showAccountDoesNotExist()

        elif response == "userBoardTitlesAndIds":
            boardTitlesAndIds = message["data"]
            
            self.__initUserBoards(boardTitlesAndIds)
            self.__ui.initBoard(boardTitlesAndIds)

        elif response == "createdBoard":
            boardTitleAndId = message["data"]
            boardDict = { boardTitleAndId['boardId']: boardTitleAndId['boardTitle']}

            self.__createBoard(boardTitleAndId)
            self.__ui.addBoard(boardDict)

        else:
            return

    def __initUser(self, username):
        self.__user = User(username)

    def __initUserBoards(self, boardTitlesAndIds):
        for boardId, boardTitle in boardTitlesAndIds.items():
            board = Board(boardTitle, boardId)

            self.__user.addBoard(board)

    def __createBoard(self, boardTitleAndId):
        boardTitle = boardTitleAndId["boardTitle"]
        boardId = boardTitleAndId["boardId"]

        self.__user.createBoard(boardTitle, boardId)

    def __handleServer(self):
        while True:
            message = self.__websocket.recv()
            message = json.loads(message)

            self.__handleMessage(message)

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
                                                    "password": password}
                                          }))

    def validatePassword(self, password):
        return True if len(password) >= 4 else False

    def sendCreateBoardToServer(self, boardTitle):
        self.__websocket.send(json.dumps({"action": "createBoard",
                                          "data": {
                                                    "boardTitle": boardTitle,
                                                    "username": self.__user.getUsername()}
                                          }))

    def sendRequestBoardDataToServer(self, boardId):
        self.__websocket.send(json.dumps({"action": "requestBoardData",
                                          "data": {
                                                    "boardId": boardId}
                                          }))
        
    def isExistedBoardTitle(self, boardTitle):
        boards = self.__user.getBoards()
        
        return boardTitle in boards.values()          

    def addUI(self, ui):
        self.__ui = ui   

if __name__ == '__main__':
    application = QApplication(sys.argv)

    bello = Bello()
    belloUI = BelloUI(None, bello)

    bello.addUI(belloUI)
    sys.exit(application.exec_())
