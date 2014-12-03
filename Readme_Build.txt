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
		
Todo:
-----
- Add progressbar when copying files (do async)
- Add much more error-checking
	* Check write protection
- Add disable run-buttons when appropriate
- Add q3config.cfg if missing
- Get Mac-version working
- More config stuff:
	* Auto download off
	* Check hunkmegs, soundmegs, zonemegs (should be max 3/4) of total RAM: Default is hunk:56, sound:8, zone:16  (max is 192 since that is the maximum used)
- Set network adapter settings to correct ip according to sickhouse.
- Clear junk option to clean out unnescessary maps etc....
- Test port option, try diagnose if firewall, network adapter down etc...
- Add get maps from sickhouse.org
- Add get maplist from sickhouse.org
- Full q3 installation (using download from onedrive options...)
- Easier UI... one big button... fix all:
	* Find quake-folder automatically
		x. If not found give option to install from onedrive
	* Check access rights
	* Check config
		x. Ask user for model
	* Update q3config
	* Create shortcut on desktop
	* Copy maps + sbpure using current session-banverk
	* Launch game after complete	