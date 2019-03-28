import os
import os.path
import sys
import subprocess as sp
import time
from . import find
#from sty import fg, rs

SIMPLE_INPUT_BANNED = (",", "*")
class cl(object):
	"""docstring for color"""
	def rojo():
		return "\033[1;92"
	
	def reboot():
		return "\033[0m"
		
def commandx(execp):
	try:
		return sp.getoutput(execp)
	except (KeyboardInterrupt, TypeError):
		pass
		
def commandy(execp):
	try:
		print(sp.run(execp, shell=True))
	except (KeyboardInterrupt, TypeError):
		pass

def line(nume=34):
	print("-"*int(nume))

def ttime(tim=0.8):
	time.sleep(int(tim))	

def dprint(txt):
	for i in txt:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write("\n")
	sys.stdout.flush()
	

def cleanInput(self, inputText):
	text = inputText
	for i in SIMPLE_INPUT_BANNED:
		text = text.replace(i)

def raiseMessage(message="All right!"):
	print(f"[+] {message}")

def raiseWarning(message="Warning!"):
	print(f"[*] {message}")

def raiseError(message="An error ocurred!"):
	print(f"[-] {message}")

def endMessage(message="Complete !"):
	print("\033[5;92m \n"+f"[+] {message}")
	print("\033[0m \033[1m")

def instalarx(nombre):

	nom = nombre.split("/")
	name = nom[1]
	print(f"[Info] Instalando {name}")
	ruta = f"tools/{name}"

	des, url, arch, ver = find.installx(nom[0], nom[1])

	print(f"[Info] Descargando {name} Porfavor espere...")
	commandx(f"git clone {url} {ruta}")
	
	try:

		if os.path.isfile(f"{ruta}/requirements.txt"):

			print(f"[Info] Instalando {ruta}/requirements.txt")
			commandx(f"pip{ver} install -r {ruta}/requirements.txt")

		elif os.path.isfile(f"{ruta}/setup.sh"):

			print(f"[Info] Instalando {ruta}/setup.sh")
			commandx(f"bash {ruta}/setup.sh")

		else:

			print("[Info] Creo que no es necesario instalar nada mas...\n[Info] Si no tendras que instalarlo de manera manual...")

	except TypeError:

		print("[Error] Algo acaba de explotar")

	a1 = name
	a2 = des

	if os.path.isfile(f"{ruta}/{arch}"):

		a3 = f"python{ver}"
		a4 = f"{name}.py"

	else:

		a3 = "bash"
		a4 = f"{name}.sh"

	a5 = nom[0]

	try:

		print(f"[Info] Creando {a5}...")
		o = commandx(f"mkdir modules/tools/{a5}")

		if o[:7] != "/bin/sh":
			print("[Info] Generacion completada!")
		else:
			print("[Info] No hace falta generar carpeta!")

		print(f"[Info] Generando modules/tools/{a5}/{a1}.py")
		x = open(f"modules/tools/{a5}/{a1}.py", "a")

		x.write(f"""
import os
from core.utils import *
from core.modules import *

class Module(BaseModule):
	def __init__(self):
		BaseModule.__init__(self)
		self.NAME = '{a1}'
		self.DESCRIPTION = '{a2}'
		# self.OPTIONS_MENU.createOptions(
				# SingleParameterOption().createOption(True, "TARGET", "Host target", default="127.0.0.1")
				
				# TARGET()
			# )

	def run(self): 
		raiseMessage("Ejecutando...")
		line()
		ttime()
		os.chdir("tools/{a1}/")
		print(commandx('sudo {a3} {arch}'))
		ttime(1)
		os.chdir("../../")
		endMessage()
""")

		x.close()
		commandx("chmod 777 modules/tools/{a5}/{a1}.py")
		print("[Info] Finalizado!")
		print("[Info] Usa reload para cargar la tool")

	except FileNotFoundError:

		print(f"Creando {a5}...")
		os.system(f"mkdir modules/tools/{a5}")

def buscarx(argumentos):

	find.searchx(argumentos)