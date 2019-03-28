tools = {
"Bruteforce":{
"instainsane":["Bruteforce instagram tools","https://github.com/thelinuxchoice/instainsane"],
"crowbar":["Crowbar es una herramienta de fuerza bruta","https://github.com/galkan/crowbar"]
},
"Informacion":{
"trape":["Geolocalizacion con una url","https://github.com/jofpin/trape", "trape.py", "2"],
"credover":["Peligros reutilización de credenciales","https://github.com/D4Vinci/Cr3dOv3r"],
"det":["(Extensible) Data Exfiltration Toolkit (DET)","https://github.com/PaulSec/DET"],
"theHarvester":["Correos electrónicos, subdominios OSINT", "https://github.com/laramies/theHarvester", "theHarvester.py", "3"],
"Infoga":["Infoga - Email OSINT","https://github.com/m4ll0k/Infoga", "infoga.py", "2"],
"webkiller":["Recopilación de información sobre herramientas","https://github.com/ultrasecurity/webkiller", "webkiller.py", "2"]
},
"Wifi":{
"fluxion":["Punto de acceso falso pishing wifi", "https://github.com/wi-fi-analyzer/fluxion"],
"wifi-hacker":["Shell Script para atacar conexiones inalámbricas", "https://github.com/esc0rtd3w/wifi-hacker"],
"wifi-deauth-attack":["Un script automatizado para el ataque de autenticación", "https://github.com/veerendra2/wifi-deauth-attack", "deauth.py", "2"],
"DDos-Attack":["Un script automatizado para el ataque de autenticación", "https://github.com/Ha3MrX/DDos-Attack", "ddos-attack.py", "2"]
},
"Pishing":{
"shellphish":["Herramienta de phishing para 18 redes sociales.","https://github.com/thelinuxchoice/shellphish"],
"whatsapp_hack":["Hack whatsapp web", "https://github.com/raptored01/whatsapp_hack", "server.py", "3"],
"Cuteit":["Ofuscador de IP", "https://github.com/D4Vinci/Cuteit", "Cuteit.py", "3"],
"Email-bomber":["Bombardeo al email", "https://github.com/zanyarjamal/Email-bomber", "E-bomber.py", "2"]
},
"Explotation":{
"avet":["Herramienta AntiVirus Evasion.","https://github.com/govolution/avet"],
"commix":["Herramienta automatizada de inyección y explotación de comandos","https://github.com/commixproject/commix"],
"gef":["GEF - Características mejoradas de GDB para los desarrolladores","https://github.com/hugsy/gef.git"],
"WPForce":["Wordpress Attack Suite","https://github.com/n00py/WPForce", "wpforce.py", "2"],
"mec":["Para explotar concurrentemente","https://github.com/jm33-m0/mec"],
"Powershell-RAT":["Gmail para filtrar datos a través de un archivo adjunto","https://github.com/Viralmaniar/Powershell-RAT"],
"HackTheWorld":["Genera cargas útiles que omite todos los antivirus","https://github.com/stormshadow07/HackTheWorld", "HackTheWorld.py", "2"],
"XSStrike":["La suite de detección XSS más avanzada","https://github.com/s0md3v/XSStrike", "xsstrike.py", "3"],
"fsociety":["Fsociety Hacking Tools Pack","https://github.com/Manisso/fsociety", "fsociety.py", "2"]
}
}

#"nombre":["descripcion", "url github", "ejecutable", "ver python"],
def installx(categoria, nombre):
	try:
		return tools[categoria][nombre][0], tools[categoria][nombre][1], tools[categoria][nombre][2], tools[categoria][nombre][3]
	except KeyError:
		print(f"No se encuentra {nombre}")

def searchx(argumentos):
	esp = " "
	opt = str((' '.join(tools))).split(" ")
	try:
		if argumentos[0] == "all":
			for x in tools:
				print("[+] "+''.join(x))
				for y in tools[x]:
					print("      "+''.join(y)+f"{esp*(30-len(''.join(y)))}{tools[x][y][0]}")
		elif argumentos[0] in opt:
			for y in tools[argumentos[0]]:
				print(''.join(y)+f"{esp*(30-len(''.join(y)))}{tools[argumentos[0]][y][0]}")
		else:
			for x in tools:
				print("[+] "+''.join(x))
		
	except KeyError:
		pass

def intools(s):
	categoria, nombre = s.split("/")
	try:
		tools[categoria][nombre]
		return True
	except:
		return False