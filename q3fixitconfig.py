import os
import shutil
import io
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import q3fixitconfig_ui

class ConfigUI(QtGui.QDialog, q3fixitconfig_ui.Ui_Q3FixitConfig):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.Q3Path = ""
        self.Players = [PlayerModel("titte", "Titte"), PlayerModel("agent", "Agent"),
                        PlayerModel("cleansweep", "Cleansweep"), PlayerModel("donhakon", "Don Hakon"),
                        PlayerModel("atomic", "Atomic"), PlayerModel("butcher", "Butcher"),
                        PlayerModel("finalinsult", "Final Insult"), PlayerModel("hanseman", "Hanseman"),
                        PlayerModel("herton", "Herton"), PlayerModel("joensson", "Joensson"),
                        PlayerModel("mega", "Mega"),
                        PlayerModel("netman", "Netman"), PlayerModel("mrego", "Mr Ego"),
                        PlayerModel("Klesk", "Shooter"), PlayerModel("Xaero", "Hellboy")]
        for p in self.Players:
            self.ModelCombo.addItem(p.Name)

        self.BrowseBtn.clicked.connect(self.BrowseQ3Folder)
        self.RunBtn.clicked.connect(self.Run)

    def find(self,f, seq):
      for item in seq:
        if f(item):
          return item

    def Run(self):

        configFilename = os.path.join(self.Q3Path, "missionpack", "q3config.cfg")
        if os.path.exists(configFilename):
            # Read config
            with open(configFilename, newline='') as f:
                data = f.readlines()

            # Update config
            if self.ModelChk.isChecked():
                selectedModelName = str(self.ModelCombo.currentText())
                player = self.find(lambda model: model.Name == selectedModelName, self.Players)
                self.SetValue(data, "seta name", player.Name)

            # Write config
            with open(configFilename, 'w', newline='') as outf:
                outf.writelines(data)

    def SetValue(self, data, key, value):
        foundRowIndex = 0
        for index, row in enumerate(data):
            if key in row:
                foundRowIndex = index
                break

        newRow = str(key + ' "' + value + '"\n')
        if foundRowIndex > 0:
            data[index] = newRow
        else:
            data.append(newRow)
    #     self.FolderText.setReadOnly(True)
    #     self.BrowseBtn.clicked.connect(self.BrowseQ3Folder)
    #     self.MapCheckerBtn.clicked.connect(self.CheckMaps)

    #     #self.Q3Path = ""
    #
    # def CheckMaps(self):
    #     currentdir = os.getcwd()
    #     mapChecker = MapChecker(self.listView)
    #     mapChecker.CheckMaps(currentdir, self.Q3Path)
    #
    def BrowseQ3Folder(self):
        q3File = QtGui.QFileDialog.getOpenFileName(self, caption="Select Quake3.exe", directory=".",
                                                filter="Exe Files (quake3.exe)")
        print(q3File)
        self.Q3Path = os.path.dirname(q3File)
        print(self.Q3Path)
        self.FolderText.setText(QtCore.QDir.toNativeSeparators(q3File))
        self.setFocus()



class PlayerModel:
    def __init__(self, model, name):
        self.Model = model
        self.Name = name


app = QtGui.QApplication(sys.argv)
dialog = ConfigUI()
#s = PlayerModel()
dialog.show()
app.exec_()
