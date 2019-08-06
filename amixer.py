import os
import sys

print(sys.version)
uu = input("===>/+/- ")


tt = int(input("====> "))

class abdo:
    def voladd(self,n):
        self.n=n
        
        self.volad = os.system("amixer set 'Master' {}%+".format(self.n))
        
        print(os.system('clear'))
        return self.volad
    def addvolim(self,k):
        self.k=k
        self.addvoli = os.system("amixer set 'Master' {}%-".format(self.k))
        print(os.system('clear'))
        return self.addvoli
        
bb = abdo()
if uu == "+":
    print(bb.voladd(tt))
elif uu == "-":
    print(bb.addvolim(tt))