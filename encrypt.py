from hashlib import *
from termcolor import *
from time import *
p1 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
sleep(1)
print(colored(p1,'red'))
p2 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
sleep(0.1)
print(colored(p2,'red'))
p3 = "-------script creat hash anf file------------------"
sleep(1)
print(colored(p3,'blue'))
p4 = "-------script creat hash anf file------------------"
sleep(0.1)
print(colored(p4,'blue'))
p5 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
sleep(1)
print(colored(p5,'red'))
p6 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
sleep(0.1)
print(colored(p6,'red'))


def main():
    #f1 = input("hahs ")
    gg = input("The file<<encrypt md5/sha224/sha1/sha384>> ")
    f2 = input("===> name file")
    with open(f2, mode="r")as f:

        for i in f:
            if gg == "md5":
                fo = md5(i.encode()).hexdigest()
                sleep(1)
                print(fo)
            elif gg == "sha224":
                ho = sha224(i.encode()).hexdigest()
                sleep(1)
                print(ho)
            elif gg == "sha1":
                do = sha1(i.encode()).hexdigest()
                sleep(1)
                print(do)
            elif gg == "sha384":
                so = sha3_384(i.encode()).hexdigest()
                sleep(1)
                print(so)

main()
