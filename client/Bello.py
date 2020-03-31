import websockets
import asyncio
import json
import sys
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\model')
from Member import Member
from Board import Board


class Bello:
    def __init__(self):
        self.__websocket = None
        self.__uri = "ws://localhost:8765"
        self.__user = None

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
            self.__initMember(username)

        elif response == "loginFail":
            print("login fail")

        elif response == "userBoardTitlesAndIds":
            boardTitlesAndIds = message["data"]

            self.__initUserBoards(boardTitlesAndIds)

        else:
            return

    def __initMember(self, username):
        self.__user = Member(username)

    def __initUserBoards(self, boardTitlesAndIds):
        for boardId, boardTitle in boardTitlesAndIds.items():
            board = Board(boardTitle, boardId)
            
            self.__user.addBoard(board)

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
        await self.__websocket.send(json.dumps({"action": "login",
                                                "data": {
                                                    "username": username,
                                                    "password": password}
                                                }))

    def verifyPassword(self, password):
        return True if len(password) >= 4 else False

    async def start(self):
        await self.__connect()

        task = asyncio.create_task(self.__handleServer())

        await task


if __name__ == '__main__':
    bello = Bello()

    asyncio.get_event_loop().run_until_complete(bello.start())
