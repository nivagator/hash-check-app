import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "M:\\Applications\\Python\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "M:\\Applications\\Python\\Python35-32\\tcl\\tk8.6"

base = None
if sys.platform == 'win32': base = 'Win32GUI'

setup(name = 'Hash Check',
    version = '0.2',
    description = 'Hash Check App',
    author = 'Gavin Greer',
    # options = {'build_exe'},
    executables = [Executable('hashcheck_v0.2.py', base = base)])
