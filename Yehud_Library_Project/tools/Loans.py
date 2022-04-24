from functools import cache
import sqlite3
from datetime import date, datetime
from flask import render_template,request

class Loans:
    con=sqlite3.connect('library.db', check_same_thread=False)
    cur=con.cursor()

    try:
        cur.execute('''CREATE TABLE Loans (CustID int,BookID int,loanDate int,returnDate int)''')
    except:
        print("table already created")
    else:
        print("table created sucessfuly")

    def loanBook(self):
        if request.method=='POST':
            loanedBooks=[]
            for row in self.cur.execute('''SELECT BookID FROM Loans WHERE returnDate=0 '''):
                loanedBooks.append(row[0])
            print(loanedBooks)
            self.CustID=request.form.get("CustID")
            self.BookID=request.form.get("BookID")
            self.loanDate=request.form.get("loanDate")
            self.cur.execute("SELECT ID FROM Books")
            self.con.commit()
            Books = self.cur.fetchall()
            flag_book=False
            for book in Books:
                if int(self.BookID)==book[0]:
                    flag_book=True

            self.cur.execute("SELECT ID FROM Customers")
            self.con.commit()
            Customers = self.cur.fetchall()
            flag_cust=False
            for cust in Customers:
                if int(self.CustID)==cust[0]:
                    flag_cust=True

            if(not flag_book and not flag_cust):
                msg="customer or book not exists in the library"
                return render_template("/Loans/loanBook.html", msg=msg)

            dt_tuple=tuple([int(x) for x in self.loanDate[:10].split('-')])
            self.loanDate=date(dt_tuple[0], dt_tuple[1], dt_tuple[2]).strftime("%d-%m-%Y")
            self.returnDate=0
            print(self.loanDate)

            if int(self.BookID) in loanedBooks:
                msg="The book is already loaned"
                print(msg)
                return render_template("/Loans/loanBook.html", msg=msg)
            else:
                print(self.CustID)
                print(self.BookID)
                print(self.loanDate)
                self.cur.execute(f'''INSERT INTO Loans VALUES({self.CustID},{self.BookID},"{self.loanDate}",{self.returnDate})''')            
                msg="The book was successfully borrowed"
                return render_template("/Loans/loanBook.html", msg=msg)
        return render_template("/Loans/loanBook.html")

    def returnBook(self):
        loanedBooks=[]
        if request.method== "POST":
            for row in self.cur.execute('''SELECT BookID FROM Loans WHERE returnDate=0 '''):
                loanedBooks.append(row[0])

            self.BookID=int(request.form.get("BookID"))
            self.returnDate=datetime.now().strftime("%d-%m-%Y")
            print(self.BookID)

            if self.BookID in loanedBooks:
                self.cur.execute(f'''UPDATE Loans SET returnDate ='{self.returnDate}' WHERE BookID={self.BookID}''')
                self.con.commit()
                msg="The book was successfully returned"
                print(msg)
                return render_template("/Loans/returnBook.html",msg=msg)
            else:
                msg="This books is not loaned"
            return render_template("/Loans/returnBook.html",msg=msg)   
        return render_template("/Loans/returnBook.html")           

    def displayAllLoans(self):
        if request.method=='GET':
            self.cur.execute('''SELECT * FROM Loans''')
            Loans = self.cur.fetchall()
            
            return render_template("/Loans/displayAllLoans.html", Loans=Loans)
        return render_template("/Loans/displayAllLoans.html")

    def displayLateLoans(self):
        if request.method=='GET':
            today=datetime.today()

            notReturned=[]
            l=self.cur.execute('''SELECT * FROM Loans WHERE returnDate=0''').fetchall()
           
            for row in l:
                notReturned.append(row)
            self.con.commit()   
            lateLoans=[]
            for book in notReturned:
                book=list(book)
                type=self.cur.execute(f'''SELECT Type FROM Books WHERE ID={int(book[1])}''').fetchone()[0]
                self.con.commit()
                loanDate=book[2]
                dt_tuple=tuple([int(x) for x in loanDate[:10].split('-')])
                loanDate=datetime(dt_tuple[2], dt_tuple[1], dt_tuple[0])
                delta=today-loanDate
                delta=int(delta.days)
                book.append(delta)
                if type==1:
                    if delta > 10:
                        lateLoans.append(book)
                elif type==2:
                    if delta > 5:
                        lateLoans.append(book)
                elif type==3:
                    if delta > 2:
                        lateLoans.append(book)
            return render_template('Loans/displaylateLoans.html',lateLoans=lateLoans)
        return render_template('Loans/displaylateLoans.html')