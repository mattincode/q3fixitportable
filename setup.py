import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(
    script = "q3fixitportable.py",
    icon = "q3f.ico",
    targetName = "Q3 MapChecker.exe",
    base = base
    )
includefiles = ["q3f.ico"]

build_options = {"include_msvcr":True, "includes" : [ "re", "atexit"], "packages": ["PyQt4.QtCore", "PyQt4.QtGui"]}
#build_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(  name = "Q3 Mapchecker",
        version = "0.1",
        description = "Q3 fixit mapchecker",
        options = {"build_exe" : build_options},
        executables = [exe])
