import config as cfg
import sys
import types

from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from mainLayoutGUI import Ui_MainWindow




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.title = 'PyQt5 layout - Synchronization files.'
        self.setWindowTitle(self.title)
        self.left = 100
        self.top = 50
        self.width = 1600
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setupUi(self)
        self.initWidgets()
        self.show()

        print("==================")





    def initWidgets(self):
        pass

        # Initialize button colours.





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()
