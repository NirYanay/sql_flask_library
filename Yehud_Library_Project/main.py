import tools.Books as tBooks
import tools.Customers as tCustomers
import tools.Loans as tLoans
from flask import Flask, render_template,request

api = Flask(__name__)
@api.route('/')
def main():
    return render_template('homePage.html')
    
@api.route('/homePage')
def home():
    return render_template('homePage.html')

@api.route('/Books')
def Books():
    return render_template('/Books/booksHomePage.html')

@api.route("/Books/addBook", methods=['GET', 'POST'])
def addBook():
    return tBooks.Book.addBook(tBooks.Book)

@api.route("/Books/displayAllBooks", methods=['GET', 'POST'])
def displayAllBooks():
    return tBooks.Book.displayAllBooks(tBooks.Book)

@api.route("/Books/removeBook",methods=['GET','POST'])
def removeBook():
    return tBooks.Book.removeBook(tBooks.Book)

@api.route("/Books/findBookByName",methods=['GET','POST'])
def findBookByName():
    return tBooks.Book.findBookByName(tBooks.Book)

@api.route('/Customers',methods=['GET','POST'])
def Customers():
    return render_template('/Customers/customersHomePage.html')

@api.route("/Customers/addNewCustomer",methods=['GET','POST'])
def addNewCustomer():
    return tCustomers.Customer.addNewCustomer(tCustomers.Customer)

@api.route("/Customers/removeCustomer",methods=['GET','POST'])
def removeCustomer():
    return tCustomers.Customer.removeCustomer(tCustomers.Customer)

@api.route("/Customers/displayAllCustomers",methods=['GET','POST'])
def displayAllCustomers():
    return tCustomers.Customer.displayAllCustomers(tCustomers.Customer)

@api.route("/Customers/findCustomerByName",methods=['GET','POST'])
def findCustomerByName():
    return tCustomers.Customer.findCustomerByName(tCustomers.Customer)

@api.route("/Loans")
def Loans():
    return render_template("/Loans/loansHomePage.html")

@api.route("/Loans/loanBook", methods=['GET','POST'])
def loanBook():
    return tLoans.Loans.loanBook(tLoans.Loans)

@api.route("/Loans/displayAllLoans",methods=['GET','POST'])
def displayLoans():
    return tLoans.Loans.displayAllLoans(tLoans.Loans)

@api.route("/Loans/returnBook",methods=['GET','POST'])
def returnBook():
    return tLoans.Loans.returnBook(tLoans.Loans)

@api.route("/Loans/displayLateLoans",methods=['GET','POST'])
def displayLateLoans():
    return tLoans.Loans.displayLateLoans(tLoans.Loans)

if __name__==("__main__"):
    api.run(debug=True,port=5500)