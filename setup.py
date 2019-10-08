import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ["os","requests","selenium"], "includes":["atexit"],"include_files":["chromedriver_v76.exe"]}

# base = None
# if sys.platform == "win32":
base = "Win32GUI"

setup(  name = "selenium_sample",
        version = "0.1",
        description = "sample selenium!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("whatsapp_automa_win_sample.py", base=base)])