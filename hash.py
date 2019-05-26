from hashlib import * 
from termcolor import *

mt = colored('################################################################################',"red")
print(mt)
print("")
print("")
slm = colored("md5","yellow")
spp = colored("sha1","yellow")
soon= colored("sha224","yellow")
slme = colored("sha256","yellow")
sppe = colored("sha384","yellow")
soone= colored("sha512","yellow")
	
tt = f"            {slm} {spp} {soon} {slme} {sppe} {soone}"
print(tt)
print("")
print("")
p = colored("################################################################################","red")
print(p)
try:
	lm = colored("md5","yellow")
	pp = colored("sha1","yellow")
	oon= colored("sha224","yellow")
	lme = colored("sha256","yellow")
	ppe = colored("sha384","yellow")
	oone= colored("sha512","yellow")
	
	#you = input("md5, sha1, sha224, sha256, sha384,sha512 ==>>> ")
	you = input(lm+" , "+pp+" , "+oon+" , "+lme+" , "+ppe+" , "+oone+" ===>>")
	has = input(colored("hash =======>>> ","white"))
	fil = input(colored("file =========>","white"))
	if you == "md5":
		oom = open(fil,mode="r")
		for i in oom:
			i=i.strip()
			if md5(i.encode()).hexdigest() == has:
				print(i)
	elif you == "sha1":
		oom = open(fil,mode="r")
		for i in oom:
			i=i.strip()
			if sha1(i.encode()).hexdigest() == has:
				print(i)		
	elif you == "sha224":
		oom = open(fil,mode="r")
		for i in oom:
			i=i.strip()
			if sha224(i.encode()).hexdigest() == has:
				print(i)	
	elif you == "sha256":
		oom = open(fil,mode="r")
		for i in oom:
			i=i.strip()
			if sha256(i.encode()).hexdigest() == has:
				print(i)	
	elif you == "sha384":
		oom = open(fil,mode="r")
		for i in oom:
			i=i.strip()
			if sha384(i.encode()).hexdigest() == has:
				print(i)				
				
	elif you == "sha512":
		oom = open(fil,mode="r")
		for i in oom:
			i=i.strip()
			if sha512(i.encode()).hexdigest() == has:
				print(i)	
			
except KeyboardInterrupt as e:
	print(e)
