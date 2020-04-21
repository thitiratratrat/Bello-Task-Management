import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class DueDateWidget(QDialog):
    def __init__(self,parent =None):
        super(DueDateWidget,self).__init__(parent)
        self.parent = parent

        self.calendar = QCalendarWidget()
        self.date = QLabel("Date: ")
        self.date.setFont(QFont("Century-Gothic",9,QFont.Bold))
        self.date.setContentsMargins(5,10,5,5)
        self.calendar.setMinimumDate(self.getMinDate())
        self.saveDateBtn = QPushButton("Save")
        self.saveDateBtn.setFont(QFont("Moon", 10, QFont.Bold))
        self.saveDateBtn.setStyleSheet(
            "background-color:rgb(250,231,110);color:rgb(49,68,111)")

        self.calendar.setLocale(QLocale.English)
        self.calendar.clicked[QDate,QLocale.English].connect(self.showDate)
        self.dueDateLayout = QVBoxLayout()
        self.dueDateLayout.addWidget(self.calendar)
        self.dueDateLayout.addWidget(self.date)
        self.dueDateLayout.addWidget(self.saveDateBtn,1,Qt.AlignCenter)
        self.setLayout(self.dueDateLayout)

    def showDate(self):
        date = self.calendar.selectedDate()
        message = "Date:  " + date.toString(Qt.ISODate)
        self.date.setText(message)
    
    def getMinDate(self):
        date = self.calendar.selectedDate()
        return date

    def getCurrentDate(self):
        date = self.calendar.selectedDate()
        self.currentDate= date.toString(Qt.ISODate)
        return self.currentDate