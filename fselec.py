from tkinter import *
from connneci import *
import fcancel
import fsearch


h_font1=('Helvetica bold',40)
h_font=('Fixedsys',40)
h_font2=('Fixedsys',24)
h_font3=('Fixedsys',18)
b_font1 = ("Times", "14",)
b_font = ("Lucida Console", "14",)
b_font3 = ("Lucida Console", "25",)
b_font2 = ("Lucida Console", "18",)

def page_funcselect(win,oldframe,modestr,db):

    functype = Frame(win,width=900,height=600)
    oldframe.forget()
    functype.tkraise()

    canvas1 = Canvas( functype, width = 900, height = 20) 
    canvas1.place(x=0,y=80) 
    canvas1.create_line(0,0,900,0,width=9,fill='white')
  

    functype.pack()

    l_heading = Label(functype,text="Function Select ",font = h_font)
    l_heading.place(x=0,y=0)

    imgbus= PhotoImage(file='bus.png')
    imgtrain= PhotoImage(file='train.png')
    imgflight= PhotoImage(file='flight.png')


    bb= Button(functype,text = "BOOK" ,font = b_font2 ,borderwidth=7,command= lambda : fsearch.page_search(win,functype,modestr,db),  width = 15,height=7)
    bt= Button(functype,text = "CANCEL" ,font = b_font2,borderwidth=7,command = lambda: fcancel.page_cancel(win,db,functype,modestr) ,width = 15,height=7)
    print("hiiii")


    bb.place(x=160,y=200)
    bt.place(x=450,y=200)
   

    pass





