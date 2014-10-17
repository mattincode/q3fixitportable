# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q3FixitConfig.ui'
#
# Created: Fri Oct 17 09:47:34 2014
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

class Ui_Q3FixitConfig(object):
    def setupUi(self, Q3FixitConfig):
        Q3FixitConfig.setObjectName(_fromUtf8("Q3FixitConfig"))
        Q3FixitConfig.resize(684, 351)
        self.gridLayout_2 = QtGui.QGridLayout(Q3FixitConfig)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Q3FixitConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.FolderText = QtGui.QLineEdit(Q3FixitConfig)
        self.FolderText.setObjectName(_fromUtf8("FolderText"))
        self.gridLayout.addWidget(self.FolderText, 1, 0, 1, 1)
        self.BrowseBtn = QtGui.QPushButton(Q3FixitConfig)
        self.BrowseBtn.setObjectName(_fromUtf8("BrowseBtn"))
        self.gridLayout.addWidget(self.BrowseBtn, 1, 1, 1, 1)
        self.RunBtn = QtGui.QPushButton(Q3FixitConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RunBtn.sizePolicy().hasHeightForWidth())
        self.RunBtn.setSizePolicy(sizePolicy)
        self.RunBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.RunBtn.setFlat(False)
        self.RunBtn.setObjectName(_fromUtf8("RunBtn"))
        self.gridLayout.addWidget(self.RunBtn, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Q3FixitConfig)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.ModelChk = QtGui.QCheckBox(self.groupBox)
        self.ModelChk.setChecked(True)
        self.ModelChk.setObjectName(_fromUtf8("ModelChk"))
        self.gridLayout_3.addWidget(self.ModelChk, 5, 0, 1, 2)
        self.LanChk = QtGui.QCheckBox(self.groupBox)
        self.LanChk.setChecked(True)
        self.LanChk.setObjectName(_fromUtf8("LanChk"))
        self.gridLayout_3.addWidget(self.LanChk, 2, 0, 1, 2)
        self.BrightnessChk = QtGui.QCheckBox(self.groupBox)
        self.BrightnessChk.setChecked(True)
        self.BrightnessChk.setObjectName(_fromUtf8("BrightnessChk"))
        self.gridLayout_3.addWidget(self.BrightnessChk, 1, 0, 1, 2)
        self.ModelCombo = QtGui.QComboBox(self.groupBox)
        self.ModelCombo.setObjectName(_fromUtf8("ModelCombo"))
        self.gridLayout_3.addWidget(self.ModelCombo, 5, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.MemoryChk = QtGui.QCheckBox(self.groupBox)
        self.MemoryChk.setChecked(True)
        self.MemoryChk.setObjectName(_fromUtf8("MemoryChk"))
        self.gridLayout_3.addWidget(self.MemoryChk, 3, 0, 1, 2)
        self.ResolutionChk = QtGui.QCheckBox(self.groupBox)
        self.ResolutionChk.setChecked(True)
        self.ResolutionChk.setObjectName(_fromUtf8("ResolutionChk"))
        self.gridLayout_3.addWidget(self.ResolutionChk, 0, 0, 1, 1)
        self.FPSChk = QtGui.QCheckBox(self.groupBox)
        self.FPSChk.setChecked(True)
        self.FPSChk.setObjectName(_fromUtf8("FPSChk"))
        self.gridLayout_3.addWidget(self.FPSChk, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Q3FixitConfig)
        QtCore.QMetaObject.connectSlotsByName(Q3FixitConfig)

    def retranslateUi(self, Q3FixitConfig):
        Q3FixitConfig.setWindowTitle(_translate("Q3FixitConfig", "Q3Fixit - Config", None))
        self.label.setText(_translate("Q3FixitConfig", "Q3 Config fixar", None))
        self.FolderText.setPlaceholderText(_translate("Q3FixitConfig", "Välj quake3.exe", None))
        self.BrowseBtn.setText(_translate("Q3FixitConfig", "Bläddra", None))
        self.RunBtn.setText(_translate("Q3FixitConfig", "Updatera Q3config!", None))
        self.groupBox.setTitle(_translate("Q3FixitConfig", "Q3 Config", None))
        self.ModelChk.setText(_translate("Q3FixitConfig", "Gör mig snygg, ange modell:", None))
        self.LanChk.setText(_translate("Q3FixitConfig", "Inget lagg tack (LAN-style)", None))
        self.BrightnessChk.setText(_translate("Q3FixitConfig", "Gör det ljust och fint", None))
        self.MemoryChk.setText(_translate("Q3FixitConfig", "Ge qvack lite minne så det flyter (hunken)", None))
        self.ResolutionChk.setText(_translate("Q3FixitConfig", "Fixa upplösningen så det blir krispigt och fint", None))
        self.FPSChk.setText(_translate("Q3FixitConfig", "Get mig optimala fps bitte (maxfps, ..)", None))

