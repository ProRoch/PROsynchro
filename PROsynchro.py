import config as cfg
import sys, os, paramiko
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
        self.lblWorking.hide()
        self.show()

        print("==================")





    def initWidgets(self):
        self.btnExit.clicked.connect(self.btn_exit)
        self.btnExecuteAction.clicked.connect(self.btnExeActionClicked)
        self.btnView.clicked.connect(self.btnRefreshView)

        listMainFolders = ["usr/RTG/etc", "commisioning", "epc"]
        listSubF_1 = ["rtg.ini","rtg_3cell.ini","rtg_4cell.ini"]
        listSubF_2 = ["Commissioning.xml", "other_Commissioning.xml","5MHz_VoLTE.xml"]
        listSubF_3 = ["epc.lua","epc_lmts.lua","My_epc.lua"]

        """
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
        """

        self.btnRefreshView()


        # Initialize button colours.


    def btnExeActionClicked(self):
        print("btn btnExeActionClicked clicked.")
        self.lblWorking.hide()
        enteredOption = 0
        for i in range(1,7):
            buttonName = self.findChild(QtWidgets.QRadioButton, "radioButton_" + str(i))
            if buttonName.isChecked():
                enteredOption = i
        print("Action set for {}".format(enteredOption))

        print("number of defined folder: {}".format(len(cfg.sync_folder)))
        remoteHost = cfg.host_PAF
        remoteHost = cfg.host_WS
        """
        "  -1-  copy file     Local    <<<-to---    WS"
        "  -2-  copy file     Local    <<<-to---  ------  <<<-to---   PAF"
        "  -3-  copy file     Local    ----to->>>   WS"
        "  -4-  copy file     Local    ----to->>> ------  ----to->>>  PAF"
        "  -5-  copy file     Local    ----to->>> - WS -  ----to->>>  PAF"
        "  -9-  exit"
        """
        if enteredOption == 1 :     #"  -1-  copy file     Local    <<<-to---   WS"
            self.copyFiles("WS","ToLocal")
        elif enteredOption == 2 :     #"  -2-  copy file     Local    <<<-to---          <<<-to---   PAF"
            self.copyFiles("PAF","ToLocal")
        elif enteredOption == 3 :     #"  -3-  copy file     Local    ----to->>>  WS"
            self.copyFiles("WS","ToRemote")
        elif enteredOption == 4 :     #"  -4-  copy file     Local    ----to->>>        ----to->>>  PAF"
            self.copyFiles("PAF","ToRemote")
        elif enteredOption == 5 :     #"  -5-  copy file     Local    ----to->>>  WS     ----to->>>  PAF"
            self.copyFiles("WS","ToRemote")
            self.copyFiles("PAF","ToRemote")
        elif enteredOption == 9 :
            print("Have a nice day...")
            quit()
        self.lblWorking.show()

    def copyFiles(self, remoteHost, cpyDirect):
        for i in range(len(cfg.sync_folder)):
            remotePC = cfg.host_WS if remoteHost == "WS" else cfg.host_PAF
            self.getFileToLocal(cfg.sync_folder[i]["dir_local"],
                              cfg.sync_folder[i]["dir_WS"] if remoteHost == "WS" else cfg.sync_folder[i]["dir_PAF"],
                              remotePC["addr"],
                              remotePC["user"],
                              remotePC["pass"] if remotePC["pkey"] == False else remotePC["pkey"],
                              cpyDirect)

    def getFileToLocal(self, localDir, remoteDir, remoteAddr, remoteUsr, remotePass=False, cpyToRemote="ToLocal"):
        localDir_full = os.getcwd() + "\\" + cfg.localFolderName + "\\" + localDir
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        try:
            k = paramiko.RSAKey.from_private_key_file(remotePass)
            ssh_client.connect(hostname=remoteAddr, username=remoteUsr, pkey=k)
        except:
            ssh_client.connect(hostname=remoteAddr, username=remoteUsr, password=remotePass)
        sftp = ssh_client.open_sftp()

        item_list = []
        if cpyToRemote == "ToRemote":
            for (dirpath, dirnames, filenames) in os.walk(localDir_full):
                for file in filenames:
                    # item_list.append(os.path.join(dirpath, file))
                    item_list.append(file)
        else:
            item_list = sftp.listdir(remoteDir)
        print("----------list files=====:{}====================".format(item_list))

        if not os.path.isdir(os.getcwd() + "\\" + cfg.localFolderName):
            os.makedirs(os.getcwd() + "\\" + cfg.localFolderName)
        if not os.path.isdir(localDir_full):
            os.makedirs(localDir_full)

        for file in item_list:
            try:
                localpath = localDir_full + "\\" + file
                remotepath = remoteDir + "/" + file
                if cpyToRemote == "ToLocal":
                    sftp.get(remotepath, localpath)
                elif cpyToRemote == "ToRemote":
                    sftp.put(localpath, remotepath)
                # print("---------------------------------")
                # print("Local path: {}".format(localpath))
                # print("Remote path: {}".format(remotepath))
                ###sftp.put(localpath, remotepath)
            except Exception as inst:
                print("Some error in copy file:{}".format(remotepath))
        sftp.close()
        ssh_client.close()


    def btnRefreshView(self):
        self.lblWorking.hide()

        i=0
        for workingFolder in cfg.sync_folder:
            treeLocal = QtWidgets.QTreeWidgetItem(self.treeMainPC)
            treeWS = QtWidgets.QTreeWidgetItem(self.treeMainWS)
            treePAF = QtWidgets.QTreeWidgetItem(self.treeMainPAF)

            treeLocal.setText(0, workingFolder["name"])
            treeWS.setText(0, workingFolder["name"])
            treePAF.setText(0, workingFolder["name"])
            #workingFolder["dir_local"]
            #workingFolder["dir_WS"]
            #workingFolder["dir_PAF"]
            #workingFolder["name"]

            item_list = []
            #for Local
            localDir_full = os.getcwd() + "\\" + cfg.localFolderName + "\\" + workingFolder["dir_local"]
            for (dirpath, dirnames, filenames) in os.walk(localDir_full):
                for file in filenames:
                    # item_list.append(os.path.join(dirpath, file))
                    item_list.append(file)
                    child = QtWidgets.QTreeWidgetItem(treeLocal)
                    child.setText(0, file)

            """
            #for WS
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
            try:
                ssh_client.connect(hostname=cfg.host_WS["addr"], username=cfg.host_WS["user"], pkey= cfg.host_WS["pkey"])
            except:
                ssh_client.connect(hostname=cfg.host_WS["addr"], username=cfg.host_WS["user"], pkey= cfg.host_WS["pass"])
            sftp = ssh_client.open_sftp()
            item_list = sftp.listdir(remoteDir)
    
            #for PAF
            """

    def btn_exit(self):
        print("btn btnExit clicked.")
        sys.exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()
