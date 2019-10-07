import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","requests","selenium"], "includes":["atexit"],"include_files":["chromedriver_v76.exe"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "WhatsBulk",
        version = "0.2",
        description = "Automate Messaging!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("wa_main_win.py", base=base)])