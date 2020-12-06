import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
					 "packages": ["pygame", "random", "sys", "threading","math","time","multiprocessing"],
					 "excludes": ['tkinter'],
					 "include_files": ['icon.png', 'start_screen.png','game_over.jpg']}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(name="Pacman",
	  version="1.0",
	  description="Catch me if u can",
	  options={"build_exe": build_exe_options},
	  executables=[Executable(script="main.py", base=base)])