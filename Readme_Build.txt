Build
-------
Create Mac App with CxFreeze: Python3 setup.py bdist_mac
Create Win-app with CxFreeze: Python setup.py build

Create GUI from ui-file
------------------------
pyuic4.bat q3fixit.ui --output q3fixit_ui.py

Icons...
-------
Until problem with cxfreeze not finding the icon-lib manual copy of png is required
Also: manual edit of the pyuic4 ui-file to load icon using:
        icon = QtGui.QIcon('q3f.png')
        Q3Fixit.setWindowIcon(icon)