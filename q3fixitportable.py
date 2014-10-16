import os
import shutil
import io
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import q3fixit_ui

class MapCheckerUI(QtGui.QDialog, q3fixit_ui.Ui_Q3Fixit):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.FolderText.setReadOnly(True)
        self.BrowseBtn.clicked.connect(self.BrowseQ3Folder)
        self.MapCheckerBtn.clicked.connect(self.CheckMaps)
        self.setFocus()
        #self.Q3Path = ""

    def CheckMaps(self):
        currentdir = os.getcwd()
        mapChecker = MapChecker(self.listView)
        mapChecker.CheckMaps(currentdir, self.Q3Path)

    def BrowseQ3Folder(self):
        q3File = QtGui.QFileDialog.getOpenFileName(self, caption="Select Quake3.exe", directory=".",
                                                filter="Exe Files (quake3.exe)")
        print(q3File)
        self.Q3Path = os.path.dirname(q3File)
        print(self.Q3Path)
        self.FolderText.setText(QtCore.QDir.toNativeSeparators(q3File))


# **** Mapchecker ****
class MapChecker:
    def __init__(self, listView):
        print("Hello")
        self.listView = listView

    def CheckMaps(self, currentdir, q3Folder):
        #currentdir = os.getcwd()
        print(currentdir)
        configDir = os.path.join(currentdir, "Quake3")
        mapsFilename = os.path.join(configDir, "maps.txt")
        mapsDir = os.path.join(currentdir, "maps")
        #q3Folder = configDir # For testing purposes
        # **** Read maps.txt ****
        mapFile = io.open(mapsFilename, 'r', encoding='utf-8-sig')
        content = mapFile.readlines()
        #print(lines)
        mapFile.close()
        model = QtGui.QStandardItemModel(self.listView)

        # mapFile = codecs.open(mapsFilename, encoding='utf-8')
        # content = mapFile.readlines()
        # mapFile.close()
        # Check if each file exists or not
        for line in content:
            s = line.strip()
            split = s.split(',')
            folder = os.path.join(q3Folder, split[0].strip())
            fileName = split[1].strip()
            fullPath = os.path.normpath(os.path.join(folder, fileName))
            copyFileName = os.path.normpath(os.path.join(mapsDir, fileName))
            copyFile = True
            item = QtGui.QStandardItem()
            if os.path.exists(fullPath):
                fileInfo = os.stat(fullPath)
                oldSize = fileInfo.st_size
                newSize = os.stat(copyFileName).st_size
                if (oldSize == newSize):
                    copyFile = False
                    item.setText("File: " + fileName + " already exist in folder: " + folder)
                    print("File: " + fileName + " already exist in folder: " + folder)

            if copyFile:
                if os.path.exists(copyFileName):
                    shutil.copyfile(copyFileName, fullPath)
                    print("Copied file: " + fileName + " to " + folder)
                    item.setText("Copied file: " + fileName + " to " + folder)
                else:
                    item.setText("Source file doesn't exist: " + fileName)

            model.appendRow(item)

        self.listView.setModel(model)
# **********************





# with open(mapsFilename) as f:
#     content = f.readlines()
# print (content)
# strings = content[0].split(',')
# print(strings[0].decode('string_escape'))

# with open(mapsFilename, 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         rowReader = csv.reader(reader)
#         for col in row:
#             print(str(row))


# for file in os.listdir(mapsDir):
#     print(file)
#     fileInfo = os.stat(os.path.join(mapsDir,file))
#     print(fileInfo.st_size)



# kolla storlek, är det samma storlek kopiera ej

app = QtGui.QApplication(sys.argv)

dialog = MapCheckerUI()
dialog.show()
app.exec_()
