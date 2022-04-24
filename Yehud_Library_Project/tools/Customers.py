from socket import MSG_CTRUNC
import sqlite3
from flask import Flask,render_template,request

class Customer:
    con=sqlite3.connect('library.db', check_same_thread=False)   
    cur = con.cursor()
    try:
        cur.execute('''CREATE TABLE Customers (
            ID int,name text,city text,age int,
            PRIMARY KEY (ID))''')
    except:
         print("table already created")
    else:
         print("table created sucessfuly")
    def addNewCustomer(self):
        msg=""
        if request.method=='POST':
            self.customerID=request.form.get("ID")
            self.customername=request.form.get("name")
            self.customercity=request.form.get("city")
            self.customerage=request.form.get("age")
            self.cur.execute("SELECT ID FROM Customers")
            self.con.commit()
            Customers = self.cur.fetchall()
            for cust in Customers:
                if int(self.customerID)==cust[0]:
                    msg="This customer already is exists in the library"
                    return render_template("/Customers/addNewCustomer.html",msg=msg)
            self.cur.execute("INSERT INTO Customers VALUES(?,?,?,?)"
            ,(self.customerID,self.customername,self.customercity,self.customerage))
            self.con.commit()
            msg="This customer added successfully to the library"
        return render_template("/Customers/addNewCustomer.html",msg=msg)

    def displayAllCustomers(self):
        self.cur.execute('''SELECT * FROM Customers''')
        Customers = self.cur.fetchall()
        self.con.commit()
        return render_template("/Customers/displayAllCustomers.html", Customers=Customers)

    def findCustomerByName(self):
        msg=""
        if request.method=="POST":
            self.name=request.form.get("name")
            self.cur.execute(f'''SELECT * FROM Customers WHERE name like "%{self.name}%"''')
            cust = self.cur.fetchall()
            self.con.commit()
            if cust==[]:
                msg="not found"
            return render_template("/Customers/findCustomerByName.html", cust=cust,msg=msg)
        return render_template("/Customers/findCustomerByName.html")

    def removeCustomer(self):
        msg=""
        if request.method=='POST':
            
            self.customerID= request.form.get('ID')
            self.cur.execute("SELECT ID FROM Customers")    
            Customers = self.cur.fetchall()
            self.con.commit()
            print("kkkkkk")
            print(Customers)
            if Customers==[]:
                msg="No customers the library"
                print(msg)
                return render_template("/Customers/removeCustomer.html",msg=msg)
                
            for cust in Customers:
                if int(self.customerID)==cust[0]:
                    self.cur.execute(f'''DELETE FROM Customers WHERE ID={self.customerID}''')
                    self.con.commit()
                    msg="This customer was removed from the library"
                    return render_template("/Customers/removeCustomer.html",msg=msg)
                else:
                    msg="This customer is not exists in the library"
            return render_template("/Customers/removeCustomer.html", msg=msg)
        return render_template("/Customers/removeCustomer.html")
