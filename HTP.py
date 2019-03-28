################################
#!/usr/bin/env python3		   #
# -*- conding: utf-8 -*-       #
################################
#	  autor: @_p1ngu1n0_       # 	   
################################

import os
import time
import random
import importlib
import core.modules

from cmd import Cmd
#from sty import fg, rs
from core.utils import *
from core.loader import *
from core.find import *

with open("path.conf", "w") as f:
	f.write(os.path.realpath(__file__)[:-len(__file__) - 1])

RANDOM_MESSAGES = ["Hack The Planet !", "\\(^v^)/\\(^v^)/\\(^v^)/\\(^v^)/\\(^v^)/", "https://p1ngu1n0.ml", "Sigueme en instagram @_p1ngu1n0_"]



def welcomeMenu(loaderObject, bannerx):
	banner = list()
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"     \            _    _            _     ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"      \          | |  | |          | |    ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"       \\        | |__| | __ _  ___| | __ ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"        \\       |  __  |/ _` |/ __| |/ / ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"         >\/7    | |  | | (_| | (__|   <  ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"     _.-(6'  \   |_|  |_|\__,_|\___|_|\_\ ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"    (=___._/` \         _   _           ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"         )  \ |        | | | |          ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"        /   / |        | |_| |__   ___  ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"       /    > /        | __| '_ \ / _ \ ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"      j    < _\        | |_| | | |  __/ ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"  _.-' :      ``.       \__|_| |_|\___| ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"  \ r=._\        `. ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r" <`\\_  \         .`-.          _____  _                  _   _  ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"  \ r-7  `-. ._  ' .  `\       |  __ \| |                | | | | ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"   \`,      `-.`7  7)   )      | |__) | | __ _ _ __   ___| |_| | ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"    \/         \|  \'  / `-._  |  ___/| |/ _` | '_ \ / _ \ __| | ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"               ||    .'        | |    | | (_| | | | |  __/ |_|_| ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"                \\  (          |_|    |_|\__,_|_| |_|\___|\__(_) ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"                 >\  > ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"             ,.-' >.' ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"            <.'_.'' ")
	banner.append("\033[0;"+str(random.randint(90, 97))+"m"+r"              <' ")
	if bannerx == True:
		for i in banner:
			print(i)
			time.sleep(0.2)
	print("\n\033[0m\033[1m----------------------------------")
	print(random.choice(RANDOM_MESSAGES))
	print(f"Cargadas Tools: {loaderObject[1]}")
	print("----------------------------------\n")


class ProgramConsole(Cmd):
	DEFAULT_PROMPT = f"root@newbie#> "
	ruler = "~"
	prompt = DEFAULT_PROMPT
	doc_header = "Documentacion de comandos (Escribe help <comand>):"
	selectedModule = None # Module selected to use. It will be used in the run, set...
	#states = ["menu", "exploit"]
	#state = str()
	loadModulesObject = None
	loadedModules = None
	RANDOM_END = ["Instalando Backdoor...", "Activando virus...", "Destruyendo dispositivo...", "Activando Webcam...", "Eliminando ficheros..."]
	banner = True
	# PROGRAM FUNCTIONS
	def startProgram(self):
		os.system("clear")
		self.loadModulesObject = loadAll() # Load modules into an object
		self.loadedModules = self.loadModulesObject[0]
		welcomeMenu(self.loadModulesObject, self.banner) # Display program information

	def menu(self):
		self.selectedModule = None
		self.prompt = self.DEFAULT_PROMPT

	def selectModule(self, module):
		if module in self.loadedModules:
			self.selectedModule = self.loadedModules[module]
		else:
			raiseError(f"Tool {module} no funciona!")
			return
		self.prompt = f"root@{self.selectedModule.NAME}#>"


	def emptyline(self): return 


	def do_reload(self, s):
		"\nReninicia el programa - reload\n"
		if s == "nobanner":
			self.banner = False
		self.startProgram()

	def do_clear(self, s):
		"\nLimpia la pantalla - clear\n"
		os.system("clear")
		banner = False
		welcomeMenu(self.loadModulesObject, banner)

	def do_exit(self, s):
		"\nSalir de HTW\n"
		os.system("clear")
		print("\n[+] "+random.choice(self.RANDOM_END))
		time.sleep(1)
		endMessage()
		sys.exit("bye bye :D\n")

	def do_menu(self, s): # Return to main menu
		"\nVuelve al menu - menu\n"
		self.menu()

	def do_show(self, s): # Show information
		"\nVisualiza las tools - show [tools/options]\n"

		try:
			esp = " "
			ray = "-"
			args = s.split()
			showOption = args[0]
			
			if showOption == "tools":
				print(f"+{ray*36}+{ray*60}+")
				print(f"|{esp*16}Tools{esp*15}|{esp*24}DESCRIPTION{esp*25}|")
				print(f"+{ray*36}+{ray*60}+")
				for module in self.loadedModules:
					if module == 20:
						pass
					print(f"|  {module}{esp*(34-len(module))}|   {self.loadedModules[module].DESCRIPTION}{esp*(57-len(self.loadedModules[module].DESCRIPTION))}|")
				print(f"+{ray*36}+{ray*60}+")
			elif showOption == "options":
				if not self.selectedModule:
					raiseError("Tool no seleccionada")
				else:
					try:
						#print ("SELECTED MODULE: " + self.selectedModule.NAME + " object: " + str(self.selectedModule))
						self.selectedModule.OPTIONS_MENU.showOptions()
					except AttributeError:
						 raiseError("No hay opciones en la tool")
		except (IndexError, UnboundLocalError):
			print("\n 	\n")
			pass

	def complete_show(self, *args):
		avalible = ["tools", "options"]

		if args:
			complete = [x for x in avalible if x.startswith(args[0])]
		else:
			complete = avalible
			
		return complete

	def do_use(self, s): # Use a module
		"\nUsa tool - use [module]\n"
		args = s.split()
		if not args:
			raiseError("Debes seleccionar una tool!")
			return
		selectedModule = args[0]
		print(f"\nSeleccionado {s} !\n")
		self.selectModule(selectedModule) 

	def complete_use(self, *args):
		if args:
			complete = [x for x in list(self.loadedModules.keys()) if x.startswith(args[0])]
		else:
			complete = list(self.loadedModules.keys())

		return complete
	
	def do_set(self, s):
		"\nSet a options - set [option]\n"
		args = s.split()

		if not self.selectedModule:
			raiseError("Ninguna tool seleccionada")
			return

		if not len(args) == 2:
			raiseError("Uso: set OPCION VALOR")
		try:
			option = args[0]
			value = args[1]
		

			self.selectedModule.OPTIONS_MENU.setOption(option, value)
			raiseMessage(f"{option} >> {value}")

		except (IndexError, AttributeError):
			pass


	def complete_set(self, *args):
		if self.selectedModule:
			if args:
				moduleOptions = self.selectedModule.getOptions()
				complete = [x for x in moduleOptions if x.startswith(args[0])]
			else:
				complete = moduleOptions

			return complete
		return None

	def do_run(self, s): # Run a module
		"\nEjecutar modulo - run\n"
		args = s.split()
		if not self.selectedModule:
			raiseError("No modulo seleccionado")
			return
		self.selectedModule.updateOptions()
		self.selectedModule.executeModule()
	
	def do_install(self, s):
		"\nInstala cualquiera de las tools disponibles con search\nUsa install categoria/tool"
		
		if "/" in s and find.intools(s):
			return instalarx(s)
		else:
			print(f"[Info] No ecuentro esa tool...")

	def do_search(self, s):
		"\nSirve para buscar las tools a instalar puedes filtrar por categorias\nUsa search para ver las categorias, usa search categorias para filtrar las tools\nde esa categoria o usa search all para visualizar todo.\n"
		argumentos = s.split(" ")
		return buscarx(argumentos)
		


mainProgram = ProgramConsole()
mainProgram.startProgram()
mainProgram.cmdloop()


