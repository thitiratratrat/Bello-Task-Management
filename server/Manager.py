from mongoengine import *
import sys

sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\classes')

from Task import Task
from Section import Section
from Board import Board
from Account import Account

connect('bello')


class Manager:
    def __deleteTaskById(self, taskId):
        task = self.__getTaskById(taskId)

        task.delete()

    def __deleteSectionById(self, sectionId):
        section = self.__getSectionById(sectionId)
        taskIds = section.task_ids

        for taskId in taskIds:
            self.__deleteTaskById(taskId)

        section.delete()

    def __getBoardById(self, boardId):
        return Board.objects.get(id=boardId)

    def __getSectionById(self, sectionId):
        return Section.objects.get(id=sectionId)

    def __getTaskById(self, taskId):
        return Task.objects.get(id=taskId)

    def __getAccountByUsername(self, usernameInput):
        return Account.objects.get(username=usernameInput)

    def getUserBoardTitlesAndIds(self, username):
        account = self.__getAccountByUsername(username)
        boardIds = account.board_ids
        boardTitlesAndIds = {}

        for boardId in boardIds:
            board = self.__getBoardById(boardId)
            boardTitlesAndIds[str(boardId)] = board.title

        return boardTitlesAndIds
    
    def getBoardDetail(self, boardId):
        board = self.__getBoardById(boardId)
        sectionIds = board.section_ids
        detail = {}

        for sectionId in sectionIds:
            sectionDetail = {}
            section = self.__getSectionById(sectionId)
            sectionTitle = section.title
            sectionDetail["title"] = sectionTitle

            taskDict = {}
            taskIds = section.task_ids

            for taskId in taskIds:
                taskDetail = {}
                task = self.__getTaskById(taskId)
                taskTitle = task.title
                taskDetail["title"] = taskTitle
                taskDetail["responsibleMembers"] = task.responsible_members
                taskDetail["dueDate"] = task.due_date
                taskDetail["comments"] = task.comments
                taskDetail["tags"] = task.tags
                taskDetail["isFinished"] = task.is_finished

                taskDict[str(taskId)] = taskDetail

            sectionDetail["task"] = taskDict

            detail[str(sectionId)] = sectionDetail

        return detail

    def isExistedUsername(self, usernameInput):
        return True if Account.objects(username=usernameInput).count() >= 1 else False

    def validateAccount(self, usernameInput, passwordInput):
        return True if Account.objects(username=usernameInput, password=passwordInput).count() == 1 else False
    
    def createAccount(self, usernameInput, passwordInput):
        account = Account(username=usernameInput, password=passwordInput)

        account.save()

    def createBoard(self, boardTitle, username):
        board = Board(title=boardTitle, members=[username])

        board.save()

        boardId = board.id
        account = self.__getAccountByUsername(username)

        account.addBoardId(boardId)

        return boardId

    def createSection(self, boardId, sectionTitle):
        section = Section(title=sectionTitle)

        section.save()

        sectionId = section.id
        board = self.__getBoardById(boardId)

        board.addSectionId(sectionId)

        return sectionId

    def createTask(self, sectionId, taskTitle, taskOrder):
        task = Task(title=taskTitle)

        task.save()

        taskId = task.id
        section = self.__getSectionById(sectionId)

        section.addTaskId(taskId, taskOrder)

        return taskId

    def editSectionTitle(self, sectionId, sectionTitle):
        section = self.__getSectionById(sectionId)

        section.editTitle(sectionTitle)

    def editTaskTitle(self, taskId, taskTitle):
        task = self.__getTaskById(taskId)

        task.editTitle(taskTitle)

    def deleteBoard(self, boardId):
        board = self.__getBoardById(boardId)
        sectionIds = board.section_ids
        memberUsernames = board.members

        for sectionId in sectionIds:
            self.__deleteSectionById(sectionId)

        for memberUsername in memberUsernames:
            account = self.__getAccountByUsername(memberUsername)
            account.removeBoardId(boardId)

        board.delete()

    def deleteSection(self, boardId, sectionId):
        board = self.__getBoardById(boardId)

        self.__deleteSectionById(sectionId)
        board.removeSectionId(sectionId)

    def deleteTask(self, sectionId, taskId):
        section = self.__getSectionById(sectionId)

        self.__deleteTaskById(taskId)
        section.removeTaskId(taskId)
        
    def deleteTaskComment(self, taskId, taskCommentOrder):
        task = self.__getTaskById(taskId)
        
        task.removeComment(taskCommentOrder)
        
    def deleteTaskTag(self, taskId, taskTag):
        task = self.__getTaskById(taskId)
        
        task.removeTag(taskTag)

    def reorderTaskInSameSection(self, sectionId, taskId, taskOrder):
        section = self.__getSectionById(sectionId)

        section.reorderTask(taskId, taskOrder)

    def reorderTaskInDifferentSection(self, sectionId, newSectionId, taskId, taskOrder):
        section = self.__getSectionById(sectionId)
        newSection = self.__getSectionById(newSectionId)

        section.removeTaskId(taskId)
        newSection.addTaskId(taskId, taskOrder)

    def addTaskComment(self, taskId, taskComment, memberUsername, taskCommentOrder):
        task = self.__getTaskById(taskId)

        task.addComment(taskComment, memberUsername, taskCommentOrder)

    def addTaskTag(self, taskId, taskTag, taskTagColor):
        task = self.__getTaskById(taskId)

        task.addTag(taskTag, taskTagColor)

    def setTaskDueDate(self, taskId, taskDueDate):
        task = self.__getTaskById(taskId)

        task.setDueDate(taskDueDate)

    def setTaskFinishState(self, taskId, taskFinishState):
        task = self.__getTaskById(taskId)

        task.setFinishState(taskFinishState)
