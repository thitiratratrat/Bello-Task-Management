from mongoengine import *


class Board(Document):
    title = StringField(required=True)
    section_ids = ListField(ObjectIdField(), default=list)
    members = ListField(StringField(), default=list)
    meta = {
        "collection": "board",
        "ordering": ["-date_created"]
    }

    def addMemberUsername(self, memberUsername):
        self.members.append(memberUsername)
        self.save()

    def addSectionId(self, sectionId):
        self.section_ids.append(sectionId)
        self.save()

    def editTitle(self, title):
        self.title = title
        
        self.save()

    def removeSectionId(self, sectionId):
        self.update(pull__section_ids=sectionId)

    def removeMemberUsername(self, memberUsername):
        self.update(pull__members=memberUsername)
