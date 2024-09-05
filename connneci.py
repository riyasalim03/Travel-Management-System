import mysql.connector
from tkinter import *



b_font = ("Times", "17",)


class cnnc:
    host="localhost"
    user="user"
    password="password"
    database="Agency"
    rowc = 0
    cancelstr="--"    
    searchstr=""
    curr_userid=NONE
    curr_date=NONE


    def __init__(self):
        self.db= mysql.connector.connect(
            host='localhost',
            user='root',
            password='tiger',
            database='Agency'
        )

    def insert_booking(self,ne,modestr,strt,dest,nos,uid,bno):

        cur = self.db.cursor()
        cur.execute("select * from booking")
        bidd = 0
        for row in cur.fetchall():
            bidd=row[0]
        
        cur.close()
        bidd = bidd+1
        str = "insert into booking values({t1},{t2},'{t3}','{t4}','{t5}',{t6},{t7});".format(
            t1=bidd,
            t2=self.curr_userid,t3=modestr,t4=strt,t5=dest,t6=nos,t7=bno
        )
        print(str)
        cur = self.db.cursor()
        cur.execute(str)

        ## updating modestr table with seat values

        str = "update {t1} set nosa=nosa-{t2} where no={t3} and day ='{t4}'".format(
            t1=modestr,t2=nos,t3=bno,t4=self.curr_date
        )
        print(str)
        cur.execute(str)
        self.db.commit()
        cur.close()


    def validate_user(self,entpass,entuser,l,next_page) -> int:

        pstr = entpass.get()
        ustr = entuser.get()
        ustr = ustr.lstrip()
        ustr = ustr.rstrip()
        pstr = pstr.strip()
        qry = "select * from cust where name='"+ustr+"';"
        cur = self.db.cursor()
        cur.execute(qry)

        row = cur.fetchone()

        if row!=None:
            if (row[1]==pstr):
                l.configure(text = "   Validated")
                self.curr_userid=row[0]
                return 1
            else:
                l.configure(text = "Wrong PassWord")
                return 0

        cur.close()




    def insert(self):
        str = ""
        cur = self.db.cursor()
        cur.execute(str)
        cur.close()
    
    def get_bookings(self,modestr) -> tuple:

        outstr = "User\tB_id\tfrom\tto\n"
        cur = self.db.cursor()
        cur.execute("select * from booking where user_id = {t1} and type = '{t2}';".format(t1=self.curr_userid,t2=modestr))
        li = []

        rows = cur.fetchall()

        for row in rows:
            li.append(row)

        cur.close()
        return li
    
    def rem_bookings(self,bid:str):
        bid = bid.lstrip()
        bid = bid.rstrip()

        """
        qry = "select nos from booking where bid="+bid+";"
        cur = self.db.cursor()
        nos = 0
        cur.execute(qry)
        
        for row in cur.fetchall():
            if row != None:
                nos=row[0]


        cur.close()
        """
        ## updating 
        ## DEleting
        qry = "delete from booking where bid="+bid+";"

        print(qry)
        cur = self.db.cursor()
        
        cur.execute(qry)
        self.db.commit()
        self.rowc = cur.rowcount
        cur.close()

        

        if self.rowc==0:
            self.cancelstr = "Bid INVALID"
        else :
            self.cancelstr = "Your Booking has been cancelled"
        print(self.cancelstr)

    def search(self,fromstr,tostr,datestr,modestr,lble)->str:
        str = "select * from {t1} where start = '{t2}' and dest = '{t3}' and day = '{t4}'".format(t1=modestr,t2=fromstr,t3=tostr,t4=datestr)
        print(str)
        cur = self.db.cursor()
        cur.execute(str)
        outstr=""
        self.curr_date = datestr
        rows = cur.fetchall()
        for row in rows:
            if row!=NONE:
                outstr += "No:{0}:\t{1} \ton {2} \tSeats Left: {3}".format(row[0],row[1],row[5],row[4])
                outstr+="\n"
                print(row)
        cur.close()
        lble.configure(text = outstr)



    