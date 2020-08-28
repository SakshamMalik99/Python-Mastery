from tkinter import *
import MySQLdb
from prettytable import PrettyTable
db = MySQLdb.connect("localhost","root","1234","d")
cursor = db.cursor()
#window = Tk()
master = Tk()
master.title("Data Base")
def del_data():
    n=e1.get()
    sql = "delete from x where name ='"+n+"'"
    #print(sql)
    cursor.execute(sql)
    db.commit()
    #print("Name: %s\nAddress: %s" % (e1.get(), e2.get()))
    print("del data")
def update_entry():
    n=e1.get()
    a=e2.get()
    sql = "update x set address='"+a+"' where name ='"+n+"'"
    #print(sql)
    cursor.execute(sql)
    db.commit()
    #print("Name: %s\nAddress: %s" % (e1.get(), e2.get()))
    print("Data Updated")
def show_data():
    sql = "SELECT * FROM x ;"
    #print("Name , Address")
    cursor.execute(sql)
    results = cursor.fetchall()
    r=5
    for row in results:
        name = row[0]
        address= row[1]
        lbl = Label(master, text=name)
        lb2 = Label(master, text=address)
        lbl.grid(column=1, row=r)
        lb2.grid(column=2, row=r)
        r=r+1
    master.mainloop()
def data_entry():
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
Button(master, text='Display', command=show_data).grid(row=0,column=3,sticky=W, pady=4)
Button(master, text='Insert', command=data_entry).grid(row=1,column=3,sticky=W, pady=4)
Button(master, text='Delete', command=del_data).grid(row=0,column=4,sticky=W, pady=4)
Button(master, text='Update', command=update_entry).grid(row=1,column=4,sticky=W, pady=4)
mainloop( )
