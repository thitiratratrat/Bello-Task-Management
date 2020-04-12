import websockets
import asyncio
import pymongo
from mongoengine import *
from bson.objectid import ObjectId
import json
import sys
sys.path.append(
    'C:\\Users\\us\\Desktop\\Y2S2\\SEP\\project\\Bello-Task-Management\\database_model')
from Section import Section
from Board import Board
from Account import Account

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
        await self.__sendUserBoardTitlesAndIdsToClient(username, websocket)

    async def __sendBoardDetail(self, data, websocket):
        boardId = data["boardId"]
        board = Board.objects.get(_id=boardId)
        sectionIds = board.section_ids
        detail = {}

        for sectionId in sectionIds:
            sectionDetail = {}
            section = Section.objects.get(_id=sectionId)
            title = section.title
            sectionDetail["title"] = title

            detail[str(sectionId)] = sectionDetail

        # TODO: get tasks
        await websocket.send(json.dumps({"response": "boardDetail",
                                         "data": {
                                             "boardId": boardId,
                                             "boardDetail": detail
                                         }}))

    async def __createBoard(self, data, websocket):
        boardTitle = data["boardTitle"]
        usernameInput = data["username"]

        boardId = ObjectId()
        board = Board(_id=boardId, title=boardTitle, members=[usernameInput])

        board.save()

        account = Account.objects.get(username=usernameInput)

        account.board_ids.append(boardId)
        account.save()

        await websocket.send(json.dumps({"response": "createdBoard",
                                         "data": {
                                             'boardTitle': boardTitle,
                                             'boardId': str(boardId)
                                         }}))

    async def __createSection(self, data, websocket):
        boardId = data["boardId"]
        sectionTitle = data["sectionTitle"]

        sectionId = ObjectId()
        section = Section(_id=sectionId, title=sectionTitle)

        section.save()

        board = Board.objects.get(_id=boardId)

        board.section_ids.append(sectionId)
        board.save()

        await websocket.send(json.dumps({"response": "createdSection",
                                         "data": {
                                             "boardId": boardId,
                                             "sectionTitle": sectionTitle,
                                             "sectionId": str(sectionId)
                                         }}))
        # TODO: notify other members

    async def __editSectionTitle(self, data, websocket):
        sectionId = data["sectionId"]
        sectionTitle = data["sectionTitle"]

        section = Section.objects.get(_id=sectionId)
        section.title = sectionTitle
        section.save()

        # TODO: notify other members

    async def __sendUserBoardTitlesAndIdsToClient(self, usernameInput, websocket):
        account = Account.objects.get(username=usernameInput)
        boardIds = account.board_ids

        boardTitles = self.__getBoardTitlesFromBoardIds(boardIds)
        await websocket.send(json.dumps({"response": "userBoardTitlesAndIds", "data": boardTitles}))

    def __getBoardTitlesFromBoardIds(self, boardIds):
        boardTitles = {}

        for boardId in boardIds:
            board = Board.objects.get(_id=boardId)
            boardTitles[str(boardId)] = board.title

        return boardTitles

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

        elif action == 'createBoard':
            await self.__createBoard(message["data"], websocket)

        elif action == 'requestBoardDetail':
            await self.__sendBoardDetail(message["data"], websocket)

        elif action == 'createSection':
            await self.__createSection(message["data"], websocket)

        elif action == 'editSectionTitle':
            await self.__editSectionTitle(message["data"], websocket)

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
