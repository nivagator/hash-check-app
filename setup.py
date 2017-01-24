import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32': base = 'Win32GUI'

setup(name = 'Hash Check',
    version = '0.2',
    description = 'Hash Check App',
    author = 'Gavin Greer',
    # options = {'build_exe'},
    executables = [Executable('hashcheck_v0.2.py', base = base)])
