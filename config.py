
localFolderName = "TL_80_RTG"

host_WS = {"addr" : "ssp-ws-macro080.macro.krk-lab.nsn-rdnet.net",
           "user" : "lmts",
           "pkey" : False,
           "pass" : "ssp123!!Macro"}

host_PAF = {"addr": "belvedere04.krk-lab.nsn-rdnet.net",
            "user": "rochumsk",
            "pkey": r"d:\PROchumski\Python\my_RSAKey\for_win",
            "pass": False}

sync_folder = []
##-----------------------------------------------------------------
new_folder = {  "dir_local" : r"usr_xxx_etc",
                "dir_WS"    : r"/usr/rtg/etc",
                "dir_PAF"   : r"/home/rochumsk/auto/sstlib_scripts/PAF/CONF/RTG/PET/CONFIGURATION/FSMr3-FDD-080",
                "name"      : "usr_xxx_etc"}
sync_folder.append(new_folder)
##-----------------------------------------------------------------

new_folder = {  "dir_local" : "WTS_BIN",
                "dir_WS"    : r"/home/lmts/WTS_BIN/configs",
                "dir_PAF"   : r"/home/rochumsk/auto/sstlib_scripts/PAF/CONF/EPCSIM/PET/FSMr3-FDD-080",
                "name"      : "wts_bin"}
sync_folder.append(new_folder)
##-----------------------------------------------------------------


new_folder = {  "dir_local" : "comiss_SBTS19A",
                "dir_WS"    : r"/home/lmts/Comissionings/SBTS19A",
                "dir_PAF"   : r"/home/rochumsk/auto/sstlib_scripts/PAF/CONF/ENB/PET/COMMISSIONING/FSM/FSMr3-FDD-080/FL19A",
                "name"      : "commissioning"}
sync_folder.append(new_folder)
##-----------------------------------------------------------------

new_folder = {  "dir_local" : "testing",
                "dir_WS"    : r"/home/lmts/PROchumski/TL80_for_testing",
                "dir_PAF"   : r"/home/rochumsk/test",
                "name"      : "for_test_script"}
#sync_folder.append(new_folder)
##-----------------------------------------------------------------


