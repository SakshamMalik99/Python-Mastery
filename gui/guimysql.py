from tkinter import *
import MySQLdb
from prettytable import PrettyTable
db = MySQLdb.connect("localhost","root","1234","d")
cursor = db.cursor()
#window = Tk()
master = Tk()
master.title("Data Base")
def show_entry_fields():
   n=e1.get()
   a=e2.get()
   sql = "insert into x values ('"+n+"','"+a+"');"
   #print(sql)
   cursor.execute(sql)
   db.commit()
   print("Name: %s\nAddress: %s" % (e1.get(), e2.get()))
Label(master, text="Name ").grid(row=0)
Label(master, text="Address ").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
#display Data in GUI
sql = "SELECT * FROM x ;"
print("Name , Address")
cursor.execute(sql)
results = cursor.fetchall()
r=10
for row in results:
    name = row[0]
    address= row[1]
    lbl = Label(master, text=name)
    lb2 = Label(master, text=address)
    lbl.grid(column=10, row=r)
    lb2.grid(column=20, row=r)
    r=r+1
master.mainloop()
mainloop( )
