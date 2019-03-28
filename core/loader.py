from core.utils import *

import os
import sys
import pyclbr
import importlib

from core.modules.base import BaseModule

try:
	MAIN_DIR = open("path.conf", "r").read()
	MODULES_FOLDER = "modules/tools"
	MODULES_DIR = MAIN_DIR +  "/" + MODULES_FOLDER
	IMPORT_DIR = MODULES_DIR[len(MAIN_DIR) + 1:]
except:
	raiseError("Can't open modules folder!")

def loadAll():
	modules = loadModules()
	generators = loadGenerators()
	return modules[0], modules[1], generators[0], generators[1] # 0 is the paths, 1 the len of loaded objects

def loadModules():
	modules_path = list()
	loaded_modules = dict()

	for subdir, dirs, files in os.walk(MODULES_DIR):
		for file in files:
			path = os.path.join(subdir, file)
			if not "__pycache__" in path:
				if file.endswith(".py"):
						module_path = path[len(MAIN_DIR) + 1:][:-3] # Module transformed into python importation
						modules_path.append(module_path)
				else:
					raiseError(f"{path} is not a valid python module!")

	for module_path in modules_path:
		try:
			module = importlib.import_module(module_path.replace("/", "."))

			if isinstance(module.Module(), BaseModule):
				loaded_modules[module_path[len(MODULES_FOLDER) + 1:]] = module.Module() # Appending the path without the modules folder to access it easly with the user input
			else:
				print(isinstance(module, BaseModule))
				raiseError(f"'{module_path}' is not a valid module! Be sure that it's extending a Module class")

		except Exception as e:
			raiseError(f"Can't import module class from '{module_path}'. \nException: {e}'")
			continue

	return loaded_modules, len(loaded_modules)

def loadGenerators():
	return dict(), 0
