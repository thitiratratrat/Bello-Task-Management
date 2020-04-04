from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from TabBar import *

class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.tabBar = TabBar(self)
        self.tabBar.tabSizeHint(0)
        self.setTabBar(self.tabBar)
        self.setTabPosition(QTabWidget.West)
