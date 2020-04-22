import websockets
import asyncio
import pymongo
import json
from Manager import Manager


class Server:
    def __init__(self):
        self.__port = 8765
        self.__address = "127.0.0.1"
        self.__manager = Manager()

    async def __signUp(self, data, websocket):
        username = data["username"]
        password = data["password"]

        if self.__manager.isExistedUsername(username):
            await websocket.send(json.dumps({"response": "existedUsername"}))
            return

        self.__manager.createAccount(username, password)
        
        await websocket.send(json.dumps({"response": "createdAccount"}))

    async def __login(self, data, websocket):
        username = data["username"]
        password = data["password"]

        if not self.__manager.validateAccount(username, password):
            await websocket.send(json.dumps({"response": "loginFail"}))
            return

        await websocket.send(json.dumps({"response": "loginSuccessful"}))
        await self.__sendUserBoardTitlesAndIdsToClient(username, websocket)

    async def __sendBoardDetail(self, data, websocket):
        boardId = data["boardId"]
        detail = self.__manager.getBoardDetail(boardId)

        await websocket.send(json.dumps({"response": "boardDetail",
                                         "data": {
                                             "boardId": boardId,
                                             "boardDetail": detail
                                         }}))

    async def __createBoard(self, data, websocket):
        boardTitle = data["boardTitle"]
        username = data["username"]

        boardId = str(self.__manager.createBoard(boardTitle, username))

        await websocket.send(json.dumps({"response": "createdBoard",
                                         "data": {
                                             'boardTitle': boardTitle,
                                             'boardId': boardId
                                         }}))

    async def __createSection(self, data, websocket):
        boardId = data["boardId"]
        sectionTitle = data["sectionTitle"]

        sectionId = str(self.__manager.createSection(boardId, sectionTitle))

        await websocket.send(json.dumps({"response": "createdSection",
                                         "data": {
                                             "boardId": boardId,
                                             "sectionTitle": sectionTitle,
                                             "sectionId": sectionId
                                         }}))

    async def __createTask(self, data, websocket):
        boardId = data["boardId"]
        sectionId = data["sectionId"]
        taskTitle = data["taskTitle"]
        taskOrder = data["taskOrder"]

        taskId = str(self.__manager.createTask(sectionId, taskTitle, taskOrder))

        await websocket.send(json.dumps({"response": "createdTask",
                                         "data": {
                                             "boardId": boardId,
                                             "sectionId": sectionId,
                                             "taskId": taskId,
                                             "taskTitle": taskTitle,
                                             "taskOrder": taskOrder
                                         }}))

    async def __editSectionTitle(self, data, websocket):
        sectionId = data["sectionId"]
        sectionTitle = data["sectionTitle"]

        self.__manager.editSectionTitle(sectionId, sectionTitle)

    async def __editTaskTitle(self, data, websocket):
        taskId = data["taskId"]
        taskTitle = data["taskTitle"]

        self.__manager.editTaskTitle(taskId, taskTitle)

    async def __deleteBoard(self, data, websocket):
        boardId = data["boardId"]
        
        self.__manager.deleteBoard(boardId)

    async def __deleteSection(self, data, websocket):
        boardId = data["boardId"]
        sectionId = data["sectionId"]
        
        self.__manager.deleteSection(boardId, sectionId)

    async def __deleteTask(self, data, websocket):
        sectionId = data["sectionId"]
        taskId = data["taskId"]
        
        self.__manager.deleteTask(sectionId, taskId)

    async def __reorderTaskInSameSection(self, data, websocket):
        sectionId = data["sectionId"]
        taskId = data["taskId"]
        taskOrder = data["taskOrder"]

        self.__manager.reorderTaskInSameSection(sectionId, taskId, taskOrder)

    async def __reorderTaskInDifferentSection(self, data, websocket):
        sectionId = data["sectionId"]
        newSectionId = data["newSectionId"]
        taskId = data["taskId"]
        taskOrder = data["taskOrder"]

        self.__manager.reorderTaskInDifferentSection(sectionId, newSectionId, taskId, taskOrder)

    async def __addTaskComment(self, data, websocket):
        taskId = data["taskId"]
        taskComment = data["taskComment"]
        memberUsername = data["memberUsername"]
        taskCommentOrder = data["taskCommentOrder"]

        self.__manager.addTaskComment(taskId, taskComment, memberUsername, taskCommentOrder)

    async def __addTaskTag(self, data, websocket):
        taskId = data["taskId"]
        taskTag = data["taskTag"]
        taskTagColor = data["taskTagColor"]

        self.__manager.addTaskTag(taskId, taskTag, taskTagColor)

    async def __setTaskDueDate(self, data, websocket):
        taskId = data["taskId"]
        taskDueDate = data["taskDueDate"]

        self.__manager.setTaskDueDate(taskId, taskDueDate)

    async def __setTaskFinishState(self, data, websocket):
        taskId = data["taskId"]
        taskFinishState = data["taskFinishState"]

        self.__manager.setTaskFinishState(taskId, taskFinishState)

    async def __sendUserBoardTitlesAndIdsToClient(self, username, websocket):
        boardTitlesAndIds = self.__manager.getUserBoardTitlesAndIds(username)
        
        await websocket.send(json.dumps({"response": "userBoardTitlesAndIds", "data": boardTitlesAndIds}))
        
    async def __handleMessage(self, message, websocket):
        action = message["action"]

        if action == 'signUp':
            await self.__signUp(message["data"], websocket)

        elif action == 'login':
            await self.__login(message["data"], websocket)

        elif action == 'createBoard':
            await self.__createBoard(message["data"], websocket)

        elif action == 'createSection':
            await self.__createSection(message["data"], websocket)

        elif action == 'createTask':
            await self.__createTask(message["data"], websocket)

        elif action == 'requestBoardDetail':
            await self.__sendBoardDetail(message["data"], websocket)

        elif action == 'editSectionTitle':
            await self.__editSectionTitle(message["data"], websocket)

        elif action == 'editTaskTitle':
            await self.__editTaskTitle(message["data"], websocket)

        elif action == 'deleteBoard':
            await self.__deleteBoard(message["data"], websocket)

        elif action == 'deleteSection':
            await self.__deleteSection(message["data"], websocket)

        elif action == 'deleteTask':
            await self.__deleteTask(message["data"], websocket)

        elif action == 'reorderTaskInSameSection':
            await self.__reorderTaskInSameSection(message["data"], websocket)

        elif action == 'reorderTaskInDifferentSection':
            await self.__reorderTaskInDifferentSection(message["data"], websocket)

        elif action == 'addTaskComment':
            await self.__addTaskComment(message["data"], websocket)

        elif action == 'addTaskTag':
            await self.__addTaskTag(message["data"], websocket)

        elif action == 'setTaskDueDate':
            await self.__setTaskDueDate(message["data"], websocket)

        elif action == 'setTaskFinishState':
            await self.__setTaskFinishState(message["data"], websocket)

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
