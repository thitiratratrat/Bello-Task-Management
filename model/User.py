from Board import Board
from Section import Section
from Task import Task


class User:
    def __init__(self, username, boards={}):
        self.__username = username
        self.__boards = boards

    def getUsername(self):
        return self.__username

    def getBoards(self):
        return self.__boards

    def createBoard(self, boardId, boardTitle):
        board = Board(boardTitle, boardId)
        self.__boards[board.getId()] = board

        board.addMemberUsername(self.__username)

    def createSection(self, boardId, sectionId, sectionTitle, tasks={}):
        board = self.__boards[boardId]
        section = Section(sectionTitle, sectionId, tasks)

        board.addSection(section)
        
    def createTask(self, boardId, sectionId, taskId, taskTitle, taskOrder, dueDate=None, responsibleMemberUsernames=set(), comments=[], tags=[]):
        board = self.__boards[boardId]
        task = Task(taskTitle, taskId, taskOrder, dueDate,
                    responsibleMemberUsernames, comments, tags)
      
        board.addTask(sectionId, task)

    def deleteBoard(self, boardId):
        self.__boards.pop(boardId, None)

    def deleteSection(self, boardId, sectionId):
        board = self.__boards[boardId]

        board.removeSection(sectionId)
        
    def deleteTask(self, boardId, sectionid, taskId):
        board = self.__boards[boardId]

        board.removeTask(sectionId, taskId)
        
    def editSectionTitle(self, boardId, sectionId, sectionTitle):
        board = self.__boards[boardId]

        board.editSectionTitle(sectionId, sectionTitle)
        
    def editTaskTitle(self, boardId, sectionId, taskId, taskTitle):
        board = self.__boards[boardId]
        
        board.editTaskTitle(sectionId, taskId, taskTitle)

    def addBoardDetail(self, boardId, boardDetail):
        for sectionId, sectionDetail in boardDetail.items():
            sectionTitle = sectionDetail["title"]
            sectionTasks = sectionDetail["task"]

            self.createSection(boardId, sectionId, sectionTitle)

            for taskId, taskDetail in sectionTasks.items():
                taskTitle = taskDetail["title"]
                responsibleMemberUsernames = taskDetail["responsibleMembers"]
                dueDate = taskDetail["dueDate"]
                comments = taskDetail["comments"]
                tags = taskDetail["tags"]

                self.createTask(boardId, sectionId, taskId, taskTitle,
                                dueDate, responsibleMemberUsernames, comments, tags)

