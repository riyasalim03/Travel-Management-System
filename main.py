from tkinter import *
from tkinter import ttk
import mysql.connector
import customtkinter as ctk

win = ctk.CTk()

win.title("AGENCY")
win.geometry('600x800')

tu = ctk.CTkEntry(win,height=2,width=200)
tu.pack()
tu.insert('end',"usename")
tp = ctk.CTkEntry(win,height=2,width=200)
tp.pack()
tp.insert('end',"password")



def bish():
    win.withdraw()
    nwin = ctk.CTk()
    tn = ctk.CTkEntry(nwin,height=2,width=20)
    nwin.geometry('600x800')
    tn.pack()
    nwin.mainloop()


b1 = ctk.CTkButton(win, text = "Next",height=2,width=20,command=bish )
g = Grid()
b1.pack()



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tiger',
    database='Agency'
)


dbcur = mydb.cursor()

dbcur.execute("select * from user;")
myres = dbcur.fetchall()

for row in myres:
    print(row)


win.mainloop()