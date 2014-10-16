import os
import shutil
import io
import sys
from PyQt4 import QtGui, QtCore
import q3fixit_ui

class MapCheckerUI(QtGui.QDialog, q3fixit_ui.Ui_Q3Fixit):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    #     layout = QtGui.QGridLayout()
    #     widget = QtGui.QDesktopWidget()
    #     screen = widget.primaryScreen()
    #     rect = widget.screenGeometry(screen)
    #     height = rect.height()
    #     width = rect.width()
    #     print(str(height) + "x" + str(width))
    #     self.label = QtGui.QLabel("Hello World!")
    #     line_edit = QtGui.QLineEdit()
    #     button = QtGui.QPushButton("Close")
    #
    #     layout.addWidget(self.label, 0, 0)
    #     layout.addWidget(line_edit, 0, 1)
    #     layout.addWidget(button, 1, 1)
    #
    #     self.setLayout(layout)
    #
    #     button.clicked.connect(self.close)
    #     line_edit.textChanged.connect(self.changeTextLabel)
    #
    # def changeTextLabel(self, text):
    #     self.label.setText(text)


# **** Mapchecker ****
class MapChecker:
    def __init__(self):

        def CheckMaps(self):
            currentdir = os.getcwd()
            print(currentdir)
            configDir = os.path.join(currentdir, "Quake3")
            mapsFilename = os.path.join(configDir, "maps.txt")
            mapsDir = os.path.join(currentdir, "maps")
            q3Folder = configDir # For testing purposes
            # **** Read maps.txt ****
            mapFile = io.open(mapsFilename, 'r', encoding='utf-8-sig')
            content = mapFile.readlines()
            #print(lines)
            mapFile.close()

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
                if os.path.exists(fullPath):
                    fileInfo = os.stat(fullPath)
                    oldSize = fileInfo.st_size
                    newSize = os.stat(copyFileName).st_size
                    if (oldSize == newSize):
                        copyFile = False
                        print("File: " + fileName + " already exist in folder: " + folder)

                if copyFile:
                    if os.path.exists(copyFileName):
                        shutil.copyfile(copyFileName, fullPath)
                        print("Copied file: " + fileName + " to " + folder)
                    else:
                        print("Source file doesn't exist: " + fileName)
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
