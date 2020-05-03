import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from CommentWidget import * 

class TaskDetailDialog(QDialog):
    def __init__(self,parent =None):
        super(TaskDetailDialog,self).__init__(parent)
        self.parent = parent

        self.taskTitleLabel = QPushButton(" Widgets")
        self.taskTitleLabel.setIcon(QIcon("images/boardIcon.png"))
        self.taskTitleLabel.setStyleSheet("background-color: rgba(0, 0, 0, 0%)")

        self.taskTitleLabel.setFont(QFont("Century Gothic", 13, QFont.Bold))
       
        self.sectionTitleLabel = QLabel("in list bello")
        self.sectionTitleLabel.setFont(QFont("Century Gothic", 8))
        self.sectionTitleLabel.setContentsMargins(20,0,10,10)

        self.tagLabel = QLabel("Tags")
        self.tagLabel.setFont(QFont("Moon",9,QFont.Bold))
       
        self.memberLabel = QLabel("Member")
        self.memberLabel.setFont(QFont("Moon",9,QFont.Bold))

        self.showTagLayout = QHBoxLayout()
        self.showTagLayout.setAlignment(Qt.AlignLeft)
        self.tag = QLabel("tag")
        self.mainTagLayout = QVBoxLayout()
        self.mainTagLayout.addWidget(self.tagLabel)
        self.mainTagLayout.addLayout(self.showTagLayout)

        self.nameAndSquare = QLabel("  C ")
        self.nameAndSquare.setFont(QFont("Moon",9,QFont.Bold))
        self.nameAndSquare.setStyleSheet("background-color: #FAE76E ;color:#31446F ")
        self.nameAndSquare.setFixedSize(20,20)
        self.mainMemberLayout = QVBoxLayout()
        self.mainMemberLayout.addWidget(self.memberLabel)

        self.memberAndTagLayout = QHBoxLayout()
        self.memberAndTagLayout.addSpacing(20)
        self.memberAndTagLayout.addLayout(self.mainMemberLayout)
        self.memberAndTagLayout.addSpacing(20)
        self.memberAndTagLayout.addLayout(self.mainTagLayout)

        self.mainDueDateLayout = QHBoxLayout()
        self.dueDateCheckBox = QCheckBox("Due date: 13-03-2020")
        self.dueDateCheckBox.setFont(QFont("Century Gothic", 9, QFont.Bold))
        self.mainDueDateLayout.addSpacing(20)

        self.commentLabel = QLabel("Show comments")
        self.commentLabel.setFont(QFont("Moon",9,QFont.Bold))
        self.commentLabel.setContentsMargins(20,0,0,0)

        self.commentLayout = QHBoxLayout()
        self.commentListWidget = QListWidget(self)

        self.addCommentBtn = QPushButton("Add")
        self.addCommentBtn.setIcon(QIcon("images/add.png"))
        self.addCommentBtn.setStyleSheet(
            "background-color:rgb(14,172,120);color:rgb(255,255,255)")
        self.addCommentBtn.setFont(QFont("Century Gothic", 7, QFont.Bold))
        self.addCommentBtn.clicked.connect(self.clickAddCommentBtn)

        self.deleteCommentBtn = QPushButton("Delete")
        self.deleteCommentBtn.setIcon(QIcon("images/delete.png"))
        self.deleteCommentBtn.setStyleSheet(
            "background-color:rgb(210,39,62);color:rgb(255,255,255)")
        self.deleteCommentBtn.setFont(QFont("Century Gothic", 7, QFont.Bold))
        self.deleteCommentBtn.clicked.connect(self.clickDelCommentButton)

        self.addAndDeleteBtnLayout = QVBoxLayout()
        self.addAndDeleteBtnLayout.setAlignment(Qt.AlignTop)
        self.addAndDeleteBtnLayout.addWidget(self.addCommentBtn)
        self.addAndDeleteBtnLayout.addWidget(self.deleteCommentBtn)

        self.commentLayout.addSpacing(20)
        self.commentLayout.addWidget(self.commentListWidget)
        self.commentLayout.addLayout(self.addAndDeleteBtnLayout)
        
        self.commentLineEdit = QLineEdit("Write a comment..")
        self.commentLineEdit.setFont(QFont("Century Gothic",7))
        self.commentLineEdit.setContentsMargins(20,10,80,30)

        self.saveBtn = QPushButton("Save")
        self.saveBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.saveBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")

        self.mainTaskDetailLayout = QVBoxLayout()
        self.mainTaskDetailLayout.addWidget(self.taskTitleLabel,1,Qt.AlignLeft)
        self.mainTaskDetailLayout.addWidget(self.sectionTitleLabel)
        self.mainTaskDetailLayout.addLayout(self.memberAndTagLayout)
        self.mainTaskDetailLayout.addSpacing(10)
        self.mainTaskDetailLayout.addLayout(self.mainDueDateLayout)
        self.mainTaskDetailLayout.addSpacing(10)
        self.mainTaskDetailLayout.addWidget(self.commentLabel)
        self.mainTaskDetailLayout.addLayout(self.commentLayout)
        self.mainTaskDetailLayout.addWidget(self.commentLineEdit)
        self.mainTaskDetailLayout.addWidget(self.saveBtn,1,Qt.AlignCenter)
        self.setLayout(self.mainTaskDetailLayout)

        self.setFixedSize(400,400)
    
    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(QColor(248, 215, 60))
        paint.setBrush(QColor(248, 215, 60))
        paint.drawEllipse(QPoint(20, 350), 90, 90)
        paint.drawEllipse(QPoint(390, 60), 75, 75)
        paint.end()
    
    def clickAddCommentBtn(self):
        if self.commentLineEdit.text() == "Write a comment..":
            return 
        else:
            member = self.parent.parent.parent.parent.getUsernameLogin()
            commentTxt = self.commentLineEdit.text()
            self.addComment(member,commentTxt)
            self.parent.parent.parent.parent.addTaskComment

    def addMemberToTask(self,memberName):
        self.nameAndSquare.setText("  " +memberName[0]+" ")
        self.mainMemberLayout.addWidget(self.nameAndSquare)

    def addComment(self,member,commentTxt):
        self.commentWidget = CommentWidget(self)
        self.commentWidget.setUser(member)
        self.commentWidget.setCommentTxt(commentTxt)
        self.commentItem = QListWidgetItem(self.commentListWidget)
        self.commentItem.setSizeHint(self.commentWidget.sizeHint())
        self.commentListWidget.addItem(self.commentItem)
        self.commentListWidget.setItemWidget(self.commentItem, self.commentWidget)
        
        #addTaskComment(self, taskId, taskComment, memberUsername, taskCommentOrder)

    def clickDelCommentButton(self):
        for selectedItem in self.commentListWidget.selectedItems():
            taskCommentOrder =self.commentListWidget.row(selectedItem)
            self.commentListWidget.takeItem(self.commentListWidget.row(selectedItem))
            taskId = self.parent.getTaskId()
            self.parent.parent.parent.parent.deleteTaskComment(taskId, taskCommentOrder)
