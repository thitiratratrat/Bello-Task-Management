from Board import Board
from Account import Account
import websockets
import asyncio
from mongoengine import *
import json
import sys
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\database_model')

connect('bello')


class Server:
    def __init__(self):
        self.__port = 8765
        self.__address = "localhost"

    async def __signUp(self, data, websocket):
        username = data["username"]
        password = data["password"]

        if self.__isExistedUsername(username):
            await websocket.send(json.dumps({"response": "existedUsername"}))
            return

        account = Account(username=username, password=password)

        account.save()
        await websocket.send(json.dumps({"response": "createdAccount"}))

    async def __login(self, data, websocket):
        username = data["username"]
        password = data["password"]

        if not self.__isValidAccount(username, password):
            await websocket.send(json.dumps({"response": "loginFail"}))
            return

        await websocket.send(json.dumps({"response": "loginSuccessful"}))
        await self.__sendUserBoardsToClient(username, websocket)

    async def __sendUserBoardNamesToClient(self, usernameInput, websocket):
        account = Account.objects(username=usernameInput)
        boardIds = account.board_id

        boardNames = self.__getBoardNamesFromBoardIds(boardIds)
        await websocket.send(json.dumps({"response": "userBoardNames", "data":  boardNames}))

    def __getBoardNamesFromBoardIds(self, boardIds):
        boardNames = []

        for boardId in boardIds:
            board = Board.objects(board_id=boardId)
            boardNames.append(board.board_title)

        return boardNames

    def __isValidAccount(self, usernameInput, passwordInput):
        return True if Account.objects(username=usernameInput, password=passwordInput).count() == 1 else False

    def __isExistedUsername(self, usernameInput):
        return True if Account.objects(username=usernameInput).count() >= 1 else False

    async def __handleMessage(self, message, websocket):
        action = message["action"]

        if action == 'signUp':
            await self.__signUp(message["data"], websocket)

        elif action == 'login':
            await self.__login(message["data"], websocket)

        else:
            return

    def getPort(self):
        return self.__port

    def getAddress(self):
        return self.__address

    async def handleClient(self, websocket, path):
        async for message in websocket:
            message = json.loads(message)

            await self.__handleMessage(message, websocket)


websocketServer = Server()
start_server = websockets.serve(
    websocketServer.handleClient, websocketServer.getAddress(), websocketServer.getPort())
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
