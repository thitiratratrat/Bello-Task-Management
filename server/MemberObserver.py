import asyncio
import websockets
import json


class MemberObserver:
    def __init__(self, username, clientWebsocket, currentBoardId=None):
        self.__username = username
        self.__currentBoardId = currentBoardId
        self.__clientWebsocket = clientWebsocket

    def getUsername(self):
        return self.__username

    def getCurrentBoardId(self):
        return self.__currentBoardId

    def getClientWebsocket(self):
        return self.__clientWebsocket

    def changeCurrentBoardId(self, boardId):
        self.__currentBoardId = boardId

    async def update(self, data, response="updateBoard"):
        await self.__clientWebsocket.send(json.dumps({"response": response,
                                         "data": data}))
