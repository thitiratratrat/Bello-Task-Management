import websocket
import threading
import json
import sys
sys.path.append(
    'C:\\Users\\us\\Desktop\\Y2S2\\SEP\\project\\Bello-Task-Management\\UI_pages')
from BelloUI import *


class Bello:
    def __init__(self):
        self.__websocket = websocket.WebSocket()
        self.__uri = "ws://127.0.0.1:8765"
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
            
        elif response == "memberUsernameDoesNotExist":
            self.__ui.signalShowMemberUsernameDoesNotExists.signalDict.emit(None)
            
            
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
            
        elif response == "addedMemberToBoard":
            self.__ui.signalAddMemberInMenuBar.signalDict.emit(None)

        elif response == "boardDetail":
            boardDetail = message["data"]
            self.__ui.goToBoardDetailPage()
           
            self.__ui.signalInitBoardDetail.signalDict.emit(boardDetail)
            
        elif response == "updateBoard":
            boardDetail = message["data"]
            self.__ui.signalUpdateBoard.signalDict.emit(boardDetail)
            
        elif response == "updateBoardTitlesAndIds":
            boardTitlesAndIds = message["data"]

            self.__ui.addBoardUpdate(boardTitlesAndIds)
       
        elif response == "deletedBoardError" :
            data = message["data"]
            deletedBoardId = data["deletedBoardId"]
            
            #TODO: show board is deleted dialog AND go to dashboard page
            self.__ui.signalDeleteBoardDialog.signalDict.emit(deletedBoardId)
            
        elif response == "deletedBoard":
            data = message["data"]
            deletedBoardId = data["deletedBoardId"]
            
            #TODO: show board is deleted dialog
            #self.__ui.signalDeleteBoardDialog.signalDict.emit(deletedBoardId)
            self.__ui.showDeletedDialog.signalDict.emit(deletedBoardId)

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
        
    def addMemberToBoard(self, boardId, memberUsername):
        self.__websocket.send(json.dumps({"action": "addMemberToBoard",
                                          "data": {
                                              "boardId": boardId,
                                              "memberUsername": memberUsername
                                          }}))
        
    def setTaskResponsibleMember(self, taskId, memberUsername):
        self.__websocket.send(json.dumps({"action": "setTaskResponsibleMember",
                                          "data": {
                                              "taskId": taskId,
                                              "memberUsername": memberUsername
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

    def deleteTask(self, sectionId, taskId):
        self.__websocket.send(json.dumps({"action": "deleteTask",
                                          "data": {
                                              "sectionId": sectionId,
                                              "taskId": taskId
                                          }}))
        
    def deleteTaskComment(self, taskId, taskCommentOrder):
        self.__websocket.send(json.dumps({"action": "deleteTaskComment",
                                          "data": {
                                              "taskId": taskId,
                                              "taskCommentOrder": taskCommentOrder
                                          }}))
        
    def deleteTaskTag(self, taskId, taskTag):
        self.__websocket.send(json.dumps({"action": "deleteTaskTag",
                                          "data": {
                                              "taskId": taskId,
                                              "taskTag": taskTag
                                          }}))
        
    def reorderTaskInSameSection(self, sectionId, taskId, taskOrder):
        self.__websocket.send(json.dumps({"action": "reorderTaskInSameSection",
                                          "data": {
                                              "sectionId": sectionId,
                                              "taskId": taskId,
                                              "taskOrder": taskOrder
                                          }}))

    def reorderTaskInDifferentSection(self, sectionId, newSectionId, taskId, taskOrder):
        self.__websocket.send(json.dumps({"action": "reorderTaskInDifferentSection",
                                          "data": {
                                              "sectionId": sectionId,
                                              "newSectionId": newSectionId,
                                              "taskId": taskId,
                                              "taskOrder": taskOrder
                                          }}))

    def sendCreateBoardToServer(self, boardTitle, username):
        self.__websocket.send(json.dumps({"action": "createBoard",
                                          "data": {
                                              "boardTitle": boardTitle,
                                              "username": username}
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
    