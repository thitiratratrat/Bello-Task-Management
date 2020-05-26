from mongoengine import *


class Account(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    board_ids = ListField(ObjectIdField(), default=list)
    meta = {'collection': 'account'}

    def addBoardId(self, boardId):
        self.board_ids.append(boardId)
        self.save()
        
    def removeBoardId(self, boardId):
        self.update(pull__board_ids=boardId)
