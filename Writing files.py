import os
from termcolor import *

p1 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
p2 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
p3 = "-------script creat text anf file------------------"
p4 = "-------script creat text anf file------------------"
p5 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"
p6 = "-------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------"

print(colored(p1,'red'))
print(colored(p2,'red'))
print(colored(p3,'blue'))
print(colored(p4,'blue'))
print(colored(p5,'red'))
print(colored(p6,'red'))




def main():

    n1 = input("Enter y/n")

    if n1 == "y":
        jo = input("enter text and file")
        if jo == "text":
            li= input("enter name text")
            go =os.mkfifo(li)
            print(go)
        elif jo == "file":
            fr = input("enter name text")
            lp = os.mkdir(fr)
            print(lp)
    else:
        print("Try again")
main()

