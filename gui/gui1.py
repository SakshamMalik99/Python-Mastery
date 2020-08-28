from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me btn  ")
btn.grid(column=1, row=0)
btn1 = Button(window, text="Click Me btn 1", bg="orange", fg="red")
btn1.grid(column=3, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!") #imp
btn2 = Button(window, text="Click Me btn 2", command=clicked)
txt = Entry(window,width=10)

def clicked1():
    lbl.configure(text="Button was clicked !!")
btn3 = Button(window, text="Click Me btn 3", command=clicked1)
txt.grid(column=1, row=3)
btn2.grid(column=0, row=3)
btn3.grid(column=0, row=4)
window.mainloop()
