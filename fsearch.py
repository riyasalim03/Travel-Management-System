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


def search_submit(db,from_entry,to_entry,date_entry,modestr,l_out,bno_lable,bno_entry,bno_button):

    db.search(from_entry.get(),to_entry.get(),date_entry.get(),modestr,l_out)
    
    bno_lable.place(x=30,y=500)
    bno_entry.place(x=30,y=530) 
    bno_button.place(x=215,y=530)

def page_search(win,oldframe,modestr,db):

    functype = Frame(win,width=900,height=600)

    oldframe.forget()
    functype.tkraise()
    functype.pack()


    canvas1 = Canvas( functype, width = 900, height = 20) 
    canvas1.place(x=0,y=80) 
    canvas1.create_line(0,0,900,0,width=9,fill='white')

    l_heading = Label(functype,text="Search",font = h_font)
    l_heading.place(x=0,y=0)

    Label(win, text="From:",font = b_font ).place(x=30, y=130)
    from_entry = Entry(win,borderwidth=5,width=20)
    from_entry.place(x=100, y=130)

    Label(win, text="To:",font = b_font ).place(x=30, y=160)
    to_entry = Entry(win,borderwidth=5,width=20)
    to_entry.place(x=100, y=160)

    Label(win, text="Date:",font = b_font ).place(x=30, y=190)
    date_entry = Entry(win,borderwidth=5,width=20)
    date_entry.insert(0,"yyyy-mm-dd")
    date_entry.place(x=100, y=190)
    l_out = Message(win,text="",font = b_font,anchor='w',width=800)
    
    
    bno_entry = Entry(win,width=20,borderwidth=5)
    bno_lable = Label(win,text="Choose Bno for Booking ",font = b_font,anchor='w')
    bno_button = Button(win, text="Book",width=20,borderwidth=5,command=lambda:page_book(win,functype,modestr,from_entry.get(),to_entry.get(),"300",db,bno_entry.get()))

    # Button to submit the form
    submit_button = Button(win, text="Submit",width=20,borderwidth=5,command=lambda:search_submit(db,from_entry,to_entry,date_entry,modestr,l_out,bno_lable,bno_entry,bno_button))
    submit_button.place(x=100, y=230)
    
    l_out.place(x=30,y=270)

    pass


def button_book_handle(entry_nos,modestr,strt,dest,nos,uid,db,bno,l_out,name_entry,tickets_entry):

    db.insert_booking(entry_nos,modestr,strt,dest,nos,uid,bno)
    l_out.configure(text="ThankYOU for Choosing Us\nDear passenger {} -{}seats has been succesfullly booked".format(name_entry.get(),tickets_entry.get()))





def page_book(win,oldframe,modestr,strt,dest,uid,db,bno_number):

    functype = Frame(win,width=900,height=600)
    oldframe.forget()
    functype.tkraise()
    functype.pack()

    canvas1 = Canvas( functype, width = 900, height = 20) 
    canvas1.place(x=0,y=80) 
    canvas1.create_line(0,0,900,0,width=9,fill='white')


    l_heading = Label(functype,text="BOOK",font = h_font)
    l_heading.place(x=0,y=0)


    Label(win, text="Passenger Name:",font = b_font).place(x=30, y=130)
    name_entry = Entry(win,borderwidth=5,width=20)
    name_entry.place(x=220, y=130)

    Label(win, text="Phone Number:",font = b_font).place(x=30, y=160)
    phone_entry = Entry(win,borderwidth=5,width=20)
    phone_entry.place(x=220, y=160)

    Label(win, text="Age:",font = b_font).place(x=30, y=190)
    age_entry = Entry(win,borderwidth=5,width=20)
    age_entry.place(x=220, y=190)

    Label(win, text="Number of Tickets:",font = b_font).place(x=30, y=220)
    tickets_entry = Entry(win,borderwidth=5,width=20)
    tickets_entry.place(x=220, y=220)
    
    l_out = Message(win,text="",font = b_font,anchor='w',width=800)

    # Button to book tickets
    book_button = Button(win,borderwidth=5,width=20,text="Book Tickets",command=lambda : button_book_handle(tickets_entry,modestr,strt,dest,tickets_entry.get(),uid,db,bno_number,l_out,name_entry,tickets_entry))
    
    book_button.place(x=220, y=260)

    l_out.place(x=30,y=370)

   

    pass





