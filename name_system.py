import platform
from termcolor import *
from time import *
import os
mt = colored('################################################################################',"red")
print(mt)
tt = """
  [system name] comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.
"""
print(tt)
p = colored("################################################################################","red")
print(p)
v = colored("Initializing program","yellow")
h = " [+] "+v
print(h)
s = "- Detecting OS...                                 "
az = colored("[ DONE ]","green")
ze = az = colored("[ DONE ]","green")
zz = "- Checking profiles...                            "
print(s+az)
print(zz+ze)
class abdo:
	def __init__(self,n):
		self.n=n
	def age(self):
		sleep(0.1)
		print("---------------------------------------------------")
		vvv = self.n.system()
		print("   Operating system:      ",vvv)
		sleep(0.3)
		print("  ")
		pp = self.n.node()
		print("   Hostname:              ",pp)
		sleep(0.3)
		print("")
		sss = self.n.release()
		print("   Operating release:     ",sss)
		sleep(0.3)
		print("")
		dd = self.n.machine()
		print("   Hardware platform:     ",dd)
		sleep(0.3)
		print("")
		ko = self.n.version()
		print("   Program version:       ",ko)
		sleep(0.3)
		print("")
		lm = self.n.platform()
		print("   platform all           ",lm)
		print('---------------------------------------------------')
	def main(self):
		print(colored("     load average:   ","blue"))
		xo = os.system("w")
		print("   ",xo)
		print("")
		print(colored('      Filesystem:     ',"blue"))
		c = os.system('df')
		print("   ",c)
		print(" ")
		ee = colored("       hits command:    ","blue")
		print(ee)
		hui = os.system('hash')
		print(hui)

		
vv = abdo(platform)
vv.age()
vv.main()
