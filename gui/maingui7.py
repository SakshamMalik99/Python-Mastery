from tkinter import *
win=Tk()
def f1():
    m=int(ent.get())
    print(m)
win.geometry("300x300")
ent=StringVar()
e=Entry(win)
e1=Entry(win,textvariable=ent)
b1=Button(win,command=f1)
e.pack()
e1.pack()
#print(ent)
b1.pack()
win.mainloop()