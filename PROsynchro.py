import config as cfg
import sys
import types

from PyQt5 import QtWidgets, QtCore, QtGui
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

        listMainFolders = ["usr/RTG/etc", "commisioning", "epc"]
        listSubF_1 = ["rtg.ini","rtg_3cell.ini","rtg_4cell.ini"]
        listSubF_2 = ["Commissioning.xml", "other_Commissioning.xml","5MHz_VoLTE.xml"]
        listSubF_3 = ["epc.lua","epc_lmts.lua","My_epc.lua"]

        parent = QtWidgets.QTreeWidgetItem(self.treeMainPC)
        parent.setText(0, listMainFolders[0])
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, listSubF_1[0])
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, listSubF_1[1])
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, listSubF_1[2])

        parent = QtWidgets.QTreeWidgetItem(self.treeMainPC)
        parent.setText(0, listMainFolders[1])
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, listSubF_2[0])
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, listSubF_2[1])
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, listSubF_2[2])


        # Initialize button colours.





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()
