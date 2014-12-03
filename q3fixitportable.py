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
        self.listView.setStyleSheet("background-color: lightgrey")
        self.MapCheckerBtn.clicked.connect(self.CheckMaps)
        self.setFocus()
        #self.Q3Path = ""

    def CheckMaps(self):
        self.listView.setStyleSheet("background-color: green")
        currentdir = os.getcwd()
        self.listView.setStyleSheet("background-color: yellow")
        mapChecker = MapChecker(self.listView, self.MapCheckerBtn, self.simulateChk.isChecked())
        self.listView.setStyleSheet("background-color: blue")
        try:
            mapChecker.CheckMaps(currentdir, self.Q3Path)
            self.listView.setStyleSheet("background-color: white")
        except:
            model = QtGui.QStandardItemModel(self.listView)
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("Bad stuff happened!" + str(sys.exc_info()))
            model.appendRow(item)
            self.listView.setModel(model)

    def BrowseQ3Folder(self):
        q3File = QtGui.QFileDialog.getOpenFileName(self, caption="Select Quake3.exe", directory=".",
                                                filter="Exe Files (quake3.exe)")
        print(q3File)
        self.Q3Path = os.path.dirname(q3File)
        print(self.Q3Path)
        self.FolderText.setText(QtCore.QDir.toNativeSeparators(q3File))


# **** Mapchecker ****
class MapChecker:
    def __init__(self, listView, runButton, simulate):
        print("Hello")
        self.listView = listView
        self.runButton = runButton
        self.simulate = simulate

    def CheckMaps(self, currentdir, q3Folder):
        self.listView.setStyleSheet("background-color: grey")
        model = QtGui.QStandardItemModel(self.listView)
        if not os.path.exists(currentdir):
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("Aktuell katalog: " + currentdir + " saknas!")
            model.appendRow(item)
            self.listView.setModel(model)
            return
        self.listView.setStyleSheet("background-color: orange")
        #currentdir = os.getcwd()
        #print(currentdir)
        configDir = os.path.join(currentdir, "Quake3")
        if not os.path.exists(configDir):
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("q3folder: " + q3Folder + " saknas!")
            model.appendRow(item)
            self.listView.setModel(model)
            return
        self.listView.setStyleSheet("background-color: purple")
        mapsFilename = os.path.join(configDir, "maps.txt")
        if not os.path.exists(mapsFilename):
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("Map-file: " + mapsFilename + " saknas!")
            model.appendRow(item)
            self.listView.setModel(model)
            return
        self.listView.setStyleSheet("background-color: olive")
        mapsDir = os.path.join(currentdir, "maps")
        if not os.path.exists(mapsDir):
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("Map-katalogen: " + mapsDir + " saknas!")
            model.appendRow(item)
            self.listView.setModel(model)
            return
        self.listView.setStyleSheet("background-color: teal")
        #q3Folder = configDir # For testing purposes
        # **** Read maps.txt ****
        errors = 0
        try:
            mapFile = io.open(mapsFilename, 'r', encoding='utf-8-sig')
            content = mapFile.readlines()
        except FileNotFoundError:
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("Could not find file:" + mapsFilename)
            model.appendRow(item)
            self.listView.setModel(model)
            errors = 1
        except:
            item = QtGui.QStandardItem()
            item.setBackground(QtGui.QColor(255,0,0))
            item.setForeground(QtGui.QColor(255,255,255))
            item.setText("Bad stuff happened!" + str(sys.exc_info()))
            model.appendRow(item)
            self.listView.setModel(model)
            errors = 1
        finally:
            mapFile.close()

        if errors > 0:
            return

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
            if os.path.exists(fullPath) and os.path.exists(copyFileName):
                fileInfo = os.stat(fullPath)
                oldSize = fileInfo.st_size
                newSize = os.stat(copyFileName).st_size
                if (oldSize == newSize):
                    copyFile = False
                    item.setBackground(QtGui.QColor(0,255,0))
                    item.setText("Fil: " + fileName + " finns redan på plats i katalog: " + folder)
                    #print("File: " + fileName + " already exist in folder: " + folder)
            else:
                errors = 1
                if not os.path.exists(copyFileName):
                    item.setBackground(QtGui.QColor(255,0,0))
                    item.setForeground(QtGui.QColor(255,255,255))
                    item.setText("Källfil(USB): " + copyFileName + " saknas!")
                    copyFile = False
                else:
                    item.setBackground(QtGui.QColor(255,0,0))
                    item.setForeground(QtGui.QColor(255,255,255))
                    item.setText("Målfil: " + fullPath + " saknas!")

            if copyFile:
                if os.path.exists(copyFileName):
                    if self.simulate:
                        item.setBackground(QtGui.QColor(255,0,0))
                        item.setForeground(QtGui.QColor(255,255,255))
                        item.setText("Fil saknas: " + fileName + " i " + folder)
                        errors = errors + 1
                    else:
                        shutil.copyfile(copyFileName, fullPath)
                        #print("Copied file: " + fileName + " to " + folder)
                        item.setBackground(QtGui.QColor(0,255,0))
                        item.setText("Kopierat " + fileName + " till " + folder)
                else:
                    item.setBackground(QtGui.QColor(255,0,0))
                    item.setForeground(QtGui.QColor(255,255,255))
                    item.setText("Källfil saknas: " + fileName)
                    errors = errors + 1

            model.appendRow(item)

        self.listView.setModel(model)
        if errors == 0:
            self.runButton.setText("Klar!")
            self.runButton.setStyleSheet("background-color: green; color: white")
        else:
            self.runButton.setText("Försök igen!")

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
