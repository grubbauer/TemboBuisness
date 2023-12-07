import hashlib
import getpass



def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    # Hash the password before storing it
    hashed_password = hash_password(password)
    
    with open("data/userdata", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

def login(username, password):
    # Hash the entered password for comparison
    entered_password = hash_password(password)
    
    with open("data/userdata", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and entered_password == stored_password:
                return True
    return False


def helpcom():
    print("Commands for Tembo Fountain V_1.0")
    print("newsale   -   Registers a new sale")
    print("readsale  -   Prints all sales")
    print("newuser   -   Registers a new customer ")
    print("readuser   -   Prints all customers registered")
    print("newworker -   Registers a new worker")
    print("help      -   Run this command")
def enternewsale(date, sale, customer, price, sellnr, custnr):
    with open("data/sales.rtd", "a") as file:
         file.write(f"Date: {date}; Sale: {sale}; Customer: {customer}; Price: {price}; SellNr.: {sellnr}; CustNr.: {custnr}\n")
def readsales():
     with open("data/sales.rtd", "r") as file:
            salescontent = file.read()
            print(salescontent)
def registernewuser(name, custnr):
    with open("data/users.rtd", "a") as file:
        file.write(f"Name: {name}; Registered under Nr: {custnr} \n")
def readuserdata():
    with open("data/users.rtd", "r" ) as file:
        usercontent = file.read()
        print(usercontent)





# Example usage:
adminlogin = None
adminmode = None
loggedin = None


"""
Default User
admin
admin
"""





# Login
username_input = input("Enter your username: ")
password_input = getpass.getpass("Enter your password: ")

if login(username_input, password_input):
    if username_input == "admin":
        print("Login sucessful!")
        loggedin = True
        adminlogin = True
    else:
        print("Login successful!")
        loggedin = True
else:
    print("Invalid username or password.")

if loggedin:
    while True:
        command = input("Enter command: ")
        if command == "help" or "Help" or "HELP" or "hELP":
            helpcom()
        elif command == "newsale":
            
            # file.write(f"Date: {date}; Sale: {sale}; Customer: {customer}; Price: {price}; SellNr.: {sellnr}; CustNr.: {custnr}\n")
            datein = input("Enter date:                                   ")
            salein = input("Enter the product sold:                       ")
            custin = input("Enter Customer:                               ")
            pricin = input("Enter Price:                                  ")
            slnrin = input("Enter the SaleNr.:                            ")
            ctnrin = input("Enter CustomerNr:                             ")
            enternewsale(datein, salein, custin, pricin, slnrin, ctnrin)
        
        elif command == "readsale":
            readsales()
        elif command == "newuser":
            namin = input("Enter name:                                   ")
            ctrin = input("Enter Customer Nr.:                           ")
            registernewuser(namin, ctrin)
        elif command == "readuser":
            readuserdata()
        elif command == "newworker":
            if adminlogin:
                nameloc = input("Enter Username of new employee.:        ")
                numrloc = input("Enter password of new User:             ")
                register(nameloc, numrloc)
        elif command == "exit":
            exit()