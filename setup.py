import sys
from cx_Freeze import setup, Executable
import os
import tkinter
os.environ['TCL_LIBRARY'] = "M:\\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "M:\\Python\\tcl\\tk8.6"

build_exe_options = {"packages": ["os", "tkinter"], "includes": ["tkinter"]}

base = None
if sys.platform == 'win32': base = 'Win32GUI'

setup(name = 'Hash Check',
    version = '0.2',
    description = 'Hash Check App',
    author = 'Gavin Greer',
    options = {'build_exe': build_exe_options},
    executables = [Executable('hashcheck_v02.py', base = base)]
    )
