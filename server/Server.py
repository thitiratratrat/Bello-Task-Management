from functools import partial
from Account import Account
import websockets
import asyncio
from mongoengine import *
import sys
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\database_model')

connect('bello')


class Server:
    def __init__(self):
        self.__port = 8765
        self.__address = "localhost"

    def __signUp(self, data, websocket):
        username = data["username"]
        password = data["password"]

        if self.__checkExistedUsername(username):
            await websocket.send({"response": "existedUsername"})
            return

        account = Account(username=username, password=password)

        account.save()
        await websocket.send({"response": "createdAccount"})

    def __checkExistedUsername(self, usernameInput):
        return True if Account.objects(username=usernameInput).count() >= 1 else False

    def __handleMessage(self, message, websocket):
        action = message["action"]
        data = message["data"]

        if action == 'signUp':
            self.__signUp(data, websocket)
            return
        else:
            return

    def getPort(self):
        return self.__port

    def getAddress(self):
        return self.__address

    async def handleClient(self, websocket, path):
        async for message in websocket:
            self.__handleMessage(message, websocket)


websocketServer = Server()
start_server = websockets.serve(
    websocketServer.handleClient, websocketServer.getAddress(), websocketServer.getPort())
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
