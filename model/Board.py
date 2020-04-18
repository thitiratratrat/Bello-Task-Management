

class Board:
    def __init__(self, title, id, sections={}, memberUsernames=set()):
        self.__title = title
        self.__id = id
        self.__sections = sections
        self.__memberUsernames = memberUsernames

    def getId(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getMemberUsernames(self):
        return self.__memberUsernames

    def addMemberUsername(self, username):
        self.__memberUsernames.add(username)

    def getSections(self):
        return self.__sections

    def addSection(self, section):
        self.__sections[section.getId()] = section

    def removeSection(self, sectionId):
        return self.__sections.pop(sectionId, None)

    def editSectionTitle(self, sectionId, newSectionTitle):
        section = self.__sections[sectionId]

        section.editTitle(newSectionTitle)
        
    def editTaskTitle(self, sectionId, taskId, taskTitle):
        section = self.__sections[sectionId]
        
        section.editTaskTitle(taskId, taskTitle)

    def addTask(self, sectionId, taskOrder, task):
        section = self.__sections[sectionId]
        
        section.addTask(taskOrder, task)
        
    def addTaskComment(self, sectionId, taskId, taskComment):
        section = self.__sections[sectionId]
        
        section.addTaskComment(taskId, taskComment)
        
    def removeTask(self, sectionId, taskId):
        section = self.__sections[sectionId]
        
        return section.removeTask(taskId)
        
    def reorderTaskInSameSection(self, sectionId, taskId, taskOrder):
        section = self.__sections[sectionId]

        section.reorderTaskInSameSection(taskId, taskOrder)