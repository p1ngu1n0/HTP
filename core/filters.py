#from core.utils import *

lowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upperLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

letters = [
		'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 
		'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
	]

def ipFilter(host):
	print(host.split("."))
	ip1 = int(host[0])
	ip2 = int(host[1])
	ip3 = int(host[3])
	#ip1, ip2, ip3 = host.split(".")
	if ip1<255 and ip2<255 and ip3<255:
		print(host)
	else:
		print("Error ip")
