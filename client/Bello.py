import websockets
import asyncio
import json
from PySide2.QtCore import *
import sys
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\model')
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\UI_pages')

from Board import Board
from User import User
from BelloUI import *


class Bello:
    def __init__(self):
        self.__websocket = None
        self.__uri = "ws://localhost:8765"
        self.__user = None
        self.__ui = None

    async def __connect(self):
        self.__websocket = await websockets.client.connect(self.__uri)
        await self.__websocket.send(json.dumps({"action": "connected"}))

    def __handleMessage(self, message):
        response = message["response"]

        if response == "existedUsername":
            print("existed username! Fail to create account!")

        elif response == "createdAccount":
            print("account created successsfully")

        elif response == "loginSuccessful":
            print("login successful!")
            self.__initUser(username)

        elif response == "loginFail":
            print("login fail")

        elif response == "userBoardTitlesAndIds":
            boardTitlesAndIds = message["data"]

            self.__initUserBoards(boardTitlesAndIds)

        elif response == "createdBoard":
            boardTitleAndId = message["data"]

            self.__createBoard(boardTitleAndId)

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

    async def __handleServer(self):

        async for message in self.__websocket:
            message = json.loads(message)

            self.__handleMessage(message)

    async def signUp(self, username, password):
        await self.__websocket.send(json.dumps({"action": "signUp",
                                                "data": {
                                                    "username": username,
                                                    "password": password}
                                                }))

    async def login(self, username, password):
        print("send login")
        await self.__websocket.send(json.dumps({"action": "login",
                                                "data": {
                                                    "username": username,
                                                    "password": password}
                                                }))

    def verifyPassword(self, password):
        return True if len(password) >= 4 else False

    async def sendCreateBoardToServer(self, boardTitle):
        await self.__websocket.send(json.dumps({"action": "createBoard",
                                                "data": {
                                                    "boardTitle": boardTitle,
                                                    "username": self.__user.getUsername()}
                                                }))

    async def sendRequestBoardDataToServer(self, boardId):
        await self.__websocket.send(json.dumps({"action": "requestBoardData",
                                                "data": {
                                                    "boardId": boardId}
                                                }))

    async def start(self):
        await self.__connect()
        
        application = QApplication(sys.argv)
        self.__ui = BelloUI(None, self)
        
        task = asyncio.create_task(self.__handleServer())
        
        sys.exit(application.exec_())
        await task


if __name__ == '__main__':
    bello = Bello()

    asyncio.get_event_loop().run_until_complete(bello.start())
