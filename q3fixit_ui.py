# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q3FixitMapchecker.ui'
#
# Created: Thu Oct 16 16:07:34 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Q3Fixit(object):
    def setupUi(self, Q3Fixit):
        Q3Fixit.setObjectName(_fromUtf8("Q3Fixit"))
        Q3Fixit.resize(349, 456)
        Q3Fixit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_2 = QtGui.QGridLayout(Q3Fixit)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setMargin(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Q3Fixit)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.FolderText = QtGui.QLineEdit(Q3Fixit)
        self.FolderText.setObjectName(_fromUtf8("FolderText"))
        self.gridLayout.addWidget(self.FolderText, 1, 0, 1, 1)
        self.BrowseBtn = QtGui.QPushButton(Q3Fixit)
        self.BrowseBtn.setObjectName(_fromUtf8("BrowseBtn"))
        self.gridLayout.addWidget(self.BrowseBtn, 1, 1, 1, 1)
        self.listView = QtGui.QListView(Q3Fixit)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.MapCheckerBtn = QtGui.QPushButton(Q3Fixit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MapCheckerBtn.sizePolicy().hasHeightForWidth())
        self.MapCheckerBtn.setSizePolicy(sizePolicy)
        self.MapCheckerBtn.setMaximumSize(QtCore.QSize(100, 30))
        self.MapCheckerBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MapCheckerBtn.setFlat(False)
        self.MapCheckerBtn.setObjectName(_fromUtf8("MapCheckerBtn"))
        self.gridLayout_2.addWidget(self.MapCheckerBtn, 1, 0, 1, 1)

        self.retranslateUi(Q3Fixit)
        QtCore.QMetaObject.connectSlotsByName(Q3Fixit)

    def retranslateUi(self, Q3Fixit):
        Q3Fixit.setWindowTitle(_translate("Q3Fixit", "Q3Fixit", None))
        self.label.setText(_translate("Q3Fixit", "Mapchecker", None))
        self.FolderText.setPlaceholderText(_translate("Q3Fixit", "Välj quake3.exe", None))
        self.BrowseBtn.setText(_translate("Q3Fixit", "Bläddra", None))
        self.MapCheckerBtn.setText(_translate("Q3Fixit", "Kör mapchecker!", None))

