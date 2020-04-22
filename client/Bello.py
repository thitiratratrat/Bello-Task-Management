import websocket
import threading
import json
import sys
sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\UI_pages')
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
            
        elif response == "loginFail":
            self.__ui.signalShowAccountDoesNotExist.signalDict.emit(None)
            
        elif response == "userBoardTitlesAndIds":
            boardTitlesAndIds = message["data"]
            
            self.__ui.addBoard(boardTitlesAndIds)
            
        elif response == "createdBoard":
            boardDetail = message["data"]
            boardDict = {boardDetail['boardId']: boardDetail['boardTitle']}
            
            self.__ui.addBoard(boardDict)
            
        elif response == "createdSection":
            sectionDetail = message["data"]
            
            self.__ui.signalAddSection.signalDict.emit(sectionDetail)

        elif response == "createdTask":
            taskDetail = message["data"]
            
            self.__ui.signalAddTask.signalDict.emit(taskDetail)
            
        elif response == "boardDetail":
            boardDetail = message["data"]
            
            self.__ui.goToBoardDetailPage()
            self.__ui.signalInitBoardDetail.signalDict.emit(boardDetail)
            
        else:
            return

    def __handleServer(self):
        while True:
            message = self.__websocket.recv()
            message = json.loads(message)
            
            self.__handleMessage(message)
            
    def addTaskComment(self, taskId, taskComment, memberUsername, taskCommentOrder):
        self.__websocket.send(json.dumps({"action": "addTaskComment",
                                          "data": {
                                              "taskId": taskId,
                                              "taskComment": taskComment,
                                              "memberUsername": memberUsername,
                                              "taskCommentOrder": taskCommentOrder
                                          }}))
        
    def addTaskTag(self, taskId, taskTag, taskTagColor):
        self.__websocket.send(json.dumps({"action": "addTaskTag",
                                          "data": {
                                              "taskId": taskId,
                                              "taskTag": taskTag,
                                              "taskTagColor": taskTagColor
                                          }}))
        
    def setTaskDueDate(self, taskId, taskDueDate):        
        self.__websocket.send(json.dumps({"action": "setTaskDueDate",
                                          "data": {
                                              "taskId": taskId,
                                              "taskDueDate": taskDueDate
                                          }}))
        
    def setTaskFinishState(self, taskId, taskFinishState):
        self.__websocket.send(json.dumps({"action": "setTaskFinishState",
                                          "data": {
                                              "taskId": taskId,
                                              "taskFinishState": taskFinishState
                                          }}))

    def editSectionTitle(self, sectionId, sectionTitle):
        self.__websocket.send(json.dumps({"action": "editSectionTitle",
                                          "data": {
                                              "sectionId": sectionId,
                                              "sectionTitle": sectionTitle
                                          }}))

    def editTaskTitle(self, taskId, taskTitle):
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
        self.__websocket.send(json.dumps({"action": "deleteBoard",
                                          "data": {
                                              "boardId": boardId
                                          }}))

    def deleteSection(self, boardId, sectionId):
        self.__websocket.send(json.dumps({"action": "deleteSection",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionId": sectionId
                                          }}))

    def deleteTask(self, boardId, sectionId, taskId):
        self.__websocket.send(json.dumps({"action": "deleteTask",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionId": sectionId,
                                              "taskId": taskId
                                          }}))
        
    def reorderTaskInSameSection(self, boardId, sectionId, taskId, taskOrder):
        self.__websocket.send(json.dumps({"action": "reorderTaskInSameSection",
                                          "data": {
                                              "sectionId": sectionId,
                                              "taskId": taskId,
                                              "taskOrder": taskOrder
                                          }}))

    def reorderTaskInDifferentSection(self, boardId, sectionId, newSectionId, taskId, taskOrder):
        self.__websocket.send(json.dumps({"action": "reorderTaskInDifferentSection",
                                          "data": {
                                              "sectionId": sectionId,
                                              "newSectionId": newSectionId,
                                              "taskId": taskId,
                                              "taskOrder": taskOrder
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

    def sendCreateTaskToServer(self, boardId, sectionId, taskTitle, taskOrder):
        self.__websocket.send(json.dumps({"action": "createTask",
                                          "data": {
                                              "boardId": boardId,
                                              "sectionId": sectionId,
                                              "taskTitle": taskTitle,
                                              "taskOrder": taskOrder
                                          }}))

    def sendRequestBoardDetailToServer(self, boardId):
        self.__websocket.send(json.dumps({"action": "requestBoardDetail",
                                          "data": {
                                              "boardId": boardId}
                                          }))

    def addUI(self, ui):
        self.__ui = ui


if __name__ == '__main__':
    application = QApplication(sys.argv)
    bello = Bello()
    belloUI = BelloUI(None, bello)
    
    bello.addUI(belloUI)
    sys.exit(application.exec_())
