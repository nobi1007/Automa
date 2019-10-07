# from distutils.core import setup
# import py2exe
# setup(console=['myscript.py'])

from cx_Freeze import setup, Executable

setup(name = "test_exec" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("test_exec.py")])