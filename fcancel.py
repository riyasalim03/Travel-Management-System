from tkinter import *
from connneci import *


h_font1=('Helvetica bold',40)
h_font=('Fixedsys',40)
h_font2=('Fixedsys',24)
h_font3=('Fixedsys',18)
b_font1 = ("Times", "14",)
b_font = ("Lucida Console", "14",)
b_font3 = ("Lucida Console", "25",)
b_font2 = ("Lucida Console", "18",)

import tksheet as tw


def riderfunc(db,del_entry,res_label):
    ## no idea why python works like this but rquired to udatea lable values along with button updates
    db.rem_bookings(del_entry.get())
    res_label.configure(text=db.cancelstr)
    res_label.place(x=10,y=490)

def page_cancel(win,db,oldframe,modestr):

    ## first show his bookings and let him choose booking id
    ## delete based on booking id 
    oldframe.forget()
    fr_cancel = Frame(win,width=900,height=600)
    fr_cancel.tkraise()
    bookstr = db.get_bookings(modestr)

    
    canvas1 = Canvas( fr_cancel, width = 900, height = 20) 
    canvas1.place(x=0,y=80) 
    canvas1.create_line(0,0,900,0,width=9,fill='white')

    l_heading = Label(fr_cancel,text="CANCEL YOUR BOOKINGS",font = h_font)
    l_b1 = Label(fr_cancel,text="Your Bookings -- ",font = b_font3)
    #l_bookings = Label(fr_cancel,text=bookstr,font = b_font)


    l_heading.place(x=0,y=0)
    l_b1.place(x=30,y=100)
    #l_bookings.place(x=50,y=150)
    fr_cancel.pack()

    table = tw.Sheet(fr_cancel,width=800,height= 200)
    table.headers(['BooKing ID','Source', 'Destintaion', 'Tickets Booked','Transport Number'])
    table.column_width(column=0, width=150, only_set_if_too_small=False)
    table.column_width(column=1, width=150, only_set_if_too_small=False)
    table.column_width(column=2, width=150, only_set_if_too_small=False)
    table.column_width(column=3, width=150, only_set_if_too_small=False)
    table.column_width(column=4, width=150, only_set_if_too_small=False)
    
    table.enable_bindings('all')
    table.disable_bindings(
        ['rc_insert_column', 'rc_delete_column', 'edit_cell', 'delete', 'paste', 'cut', 'rc_delete_row',
         'rc_insert_row'])

    for row in bookstr:
         t1 = (row[0],)+ row[3:8]
         table.insert_row(values=t1, idx='end', add_columns=False)   
    table.place(x=30,y=150)

    del_label = Label(fr_cancel,text="Enter Bid to delete ",font = b_font) 
    del_entry = Entry(fr_cancel ,width=40,borderwidth=5 )
    res_label = Label(fr_cancel,text="-",font = b_font) 
    

    b_cancel  = Button(fr_cancel,text="Cancel",borderwidth=5,width=30,command = lambda : riderfunc(db,del_entry,res_label))
    res_label.configure(text=db.cancelstr)
    del_label.place(x=10,y=400)
    del_entry.place(x=10,y=430)
    b_cancel.place(x=310,y=430)
    res_label.place(x=10,y=490)

    

    pass

