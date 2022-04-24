import sqlite3  
from flask import render_template,request

class Book:
    con=sqlite3.connect('library.db', check_same_thread=False)   
    cur = con.cursor()

    try:
        cur.execute('''CREATE TABLE Books (
            ID int,name text,author text,yearPublished int,type int
            ,PRIMARY KEY (ID))''')
    except:
        msg="table already created"
    else:
        msg="table created sucessfuly"
    print(msg)

    def addBook(self):
        msg=""
        if request.method=='POST':
            self.bookid=request.form.get('id')
            self.bookname =request.form.get('name')
            self.author = request.form.get('author')
            self.yearPublished = request.form.get('yearPublished')
            self.type = request.form.get('type')

            self.cur.execute("SELECT ID FROM Books")
            self.con.commit()
            Books = self.cur.fetchall()
            for book in Books:
                if int(self.bookid)==book[0]:
                    msg="This book already exists in the library"
                    return render_template("/Books/addBook.html",msg=msg)

            self.cur.execute("INSERT INTO Books (ID,name,author,yearPublished,type) VALUES (?,?,?,?,?)"
            ,(self.bookid,self.bookname,self.author,self.yearPublished,self.type))
            self.con.commit()
            msg="This book added successfully to the library"
        return render_template("/Books/addBook.html",msg=msg)

    def displayAllBooks(self):
        self.cur.execute("SELECT * FROM Books")
        self.con.commit()
        Books = self.cur.fetchall()
        for book in Books:
            print(book)
        return render_template("/Books/displayAllBooks.html", Books=Books)

    def findBookByName(self):
        msg=""
        if request.method=='POST':
            self.bookName = request.form.get('bookName')
            self.cur.execute(f'''SELECT * FROM Books WHERE name like "%{self.bookName}%"''')
            Books = self.cur.fetchall()
            self.con.commit()
            if Books==[]:
                msg="not found"
            return render_template("/Books/findBookByName.html",Books=Books,msg=msg)
        return render_template("/Books/findBookByName.html")

    def removeBook(self):
        msg=""
        if request.method=='POST':
            
            self.bookid=request.form.get("ID")
            self.cur.execute("SELECT ID FROM Books")
            Books = self.cur.fetchall()
            print("kkkkkkk")
            print(Books)
            self.con.commit()
            if Books==[]:
                msg="No books in the library"
                return render_template("/Books/removeBook.html",msg=msg)
            for book in Books:
                if int(self.bookid)==book[0]:
                    self.cur.execute(f'''DELETE FROM Books WHERE ID={self.bookid}''')
                    msg="This book was removed from the library"
                    return render_template("/Books/removeBook.html",msg=msg)
                else:
                    msg="This book is not exists in the library"
            return render_template("/Books/removeBook.html", msg=msg)
        return render_template("/Books/removeBook.html")
