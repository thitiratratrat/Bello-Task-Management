import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QComboBox):
    def __init__(self):
        QComboBox.__init__(self)
        self.resize(200, 25)
        pixmap = QPixmap(20, 20)
        for color in 'red orange yellow green blue grey violet'.split():
            pixmap.fill(QColor(color))
            self.addItem(QIcon(pixmap), color.title())

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())