# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainLayoutGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(60, 110, 256, 671))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_2.setGeometry(QtCore.QRect(350, 110, 256, 671))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_3.setGeometry(QtCore.QRect(650, 120, 256, 671))
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.treeWidget_3.headerItem().setText(0, "1")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 47, 13))
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(90, 50, 185, 41))
        self.commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "New Column_2"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "New Column"))
        self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "test_1"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "test_2"))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "file_1"))
        self.treeWidget_2.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "file 2"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.treeWidget_3.headerItem().setText(1, _translate("MainWindow", "New Column_2"))
        self.treeWidget_3.headerItem().setText(2, _translate("MainWindow", "New Column"))
        self.treeWidget_3.headerItem().setText(3, _translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "test_1"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "test_2"))
        self.treeWidget_3.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "file_1"))
        self.treeWidget_3.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "file 2"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.commandLinkButton.setText(_translate("MainWindow", "scp to ws"))

