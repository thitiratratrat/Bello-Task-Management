import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Section(QListWidget):
    def __init__(self,type, parent=None):
        super(Section).__init__(parent)
        self.parent =parent
       
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDropIndicatorShown(True)


    def dragEnterEvent(self,event):
        print(event)
        if(event.mimeData().hasText()):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self,event):
        self.addItem(event.mimeData().item())
        #self.setItemWidget(self.taskItem,self.taskWidget)

    '''
    def startDrag(self, supportedActions):
        drag =  QDrag(self)
        t = [i for i in self.selectedItems()]
        mimeData = self.model().mimeData(self.selectedIndexes())
        mimeData.setText(str(t))
        drag.setMimeData(mimeData)
        if drag.start( Qt.MoveAction) ==  Qt.MoveAction:
            for item in self.selectedItems():
                self.takeItem(self.row(item))
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        else:
            event.accept()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        else:
            event.accept()
 
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        if isinstance(event.source(), Section):
            event.setDropAction(QtCore.Qt.MoveAction)
            super(Section, self).dropEvent(event)
        else:
            event.ignore()
 
    def dropMimeData(self, index, mimedata, action):
        super(Section, self).dropMimeData(index, mimedata, action)
        return True
    '''