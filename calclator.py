from tkinter import *
from  time import *
def main():
    num1 = float(bo.get())
    #print(num1)

    num2 = float(o.get())
    #print(num2)
    #sum = num1+num2
    print(vv.set(int(num1+num2)))
def kali():
    num3 = float(be.get())
    num4 = float(yy.get())
    #fdd = num3*num4
    print(ev.set(int(num3*num4)))
def poho():
    hi1 = float(abdo.get())
    hi2 = float(linux.get())
    #iee = hi1-hi2
    print(cup.set(int(hi1-hi2)))
def lolol():
    z1=float(back.get())
    z2=float(lin.get())
    #az = z1/z2
    print(upda.set(int(z1/z2)))


#num1 = int(bo.get())
#num2 = int(o.get())
#sum = num1+num2
###################################################""
root=Tk()
root.title('dehini')
root.geometry("450x600")
vv =StringVar()
ev = StringVar()
cup=StringVar()
upda=StringVar()
hohoho=StringVar()
print(hohoho.set(asctime()))

##################################################################################
bo = Entry(root,text='r',bg='cyan' )
bo.place(x=0, y=17)
tr = Label(root,text='========>>  ( + )',fg='white',bg='black')
tr.place(x=0, y=40)
o = Entry(root,text='fr',bg='cyan')
o.place(x=0, y=60)
boo = Button(root,text='=',fg='red',command=main)
#boo.bind("<ggg>")
boo.place(x=45, y=90)
mm = Entry(root,text='data====>',textvariable=vv)
mm.place(x=180,y=35)
dd = Label(root, text='*************************************************************************')
dd.place(x=0,y=120)
################################################################################
be = Entry(root,text='kk',bg='red' )
be.place(x=0, y=150)
te = Label(root,text='=========>> ( x )',fg='white',bg='black')
te.place(x=0, y=175)
yy = Entry(root,text='frede',bg='red')
yy.place(x=0, y=200)
boo = Button(root,text='=',fg='red',command=kali)
boo.place(x=45, y=227)
si = Entry(root,text='data====>',textvariable=ev)
si.place(x=180,y=170)
qq = Label(root, text='*************************************************************************')
qq.place(x=0,y=259)

abdo = Entry(root,text='kkdf',bg='cyan' )
abdo.place(x=0, y=273)
hani = Label(root,text='=======> ( - )',fg='white',bg='black')
hani.place(x=0, y=296)
linux = Entry(root,text='dfdf',bg='cyan')
linux.place(x=0, y=320)
boot = Button(root,text='=',fg='red',command=poho)
boot.place(x=45, y=345)
sie = Entry(root,text='datfdf=>',textvariable=cup)
sie.place(x=180,y=290)
jojo = Label(root, text='*************************************************************************')
jojo.place(x=0,y=373)

back = Entry(root,text='uyu',bg='cyan' )
back.place(x=0, y=387)
haho = Label(root,text='======> ( / )',fg='white',bg='black')
haho.place(x=0, y=410)
lin = Entry(root,text='tgrg',bg='cyan')
lin.place(x=0, y=433)
boott = Button(root,text='=',fg='red',command=lolol)
boott.place(x=45, y=460)
siee = Entry(root,text='datfdf',textvariable=upda)
siee.place(x=180,y=410)
qiqi = Label(root, text='_________________________________________________________________________________',bg='black')
qiqi.place(x=0,y=500)
mioo = Label(root, text='date ==> ', textvariable=hohoho)
mioo.place(x=80, y=540)
#ddii = Button(root,text='hh',command=milod)
#ddii.pack()

qitrtri = Label(root, text='_________________________________________________________________________________',bg='black')
qitrtri.place(x=0,y=570)











root.mainloop()