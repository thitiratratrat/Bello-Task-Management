from PySide2.QtCore import *

class CustomSignal(QObject):
    signalDict = Signal(dict)