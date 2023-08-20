import mysql.connector
from mysql.connector import errors
from rich import print as printc
def connectDB():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root"
        ) 
    except Exception as e:
        printc(f"[red]{e}[/red]")
    return mydb

def createDB():
    mydb = connectDB()
    mycursor = mydb.cursor()
    comList = ["CREATE DATABASE userpass",
               "USE userpass",
               "CREATE TABLE userlist(user VARCHAR(225), password VARCHAR(225), PRIMARY KEY (user))",
               "CREATE TABLE passlist(user VARCHAR(225),webName VARCHAR(225) NOT NULL, url VARCHAR(225) NOT NULL, mail VARCHAR(225) NOT NULL, id VARCHAR(225) NOT NULL, password VARCHAR(225) NOT NULL, note VARCHAR(225), encryptionKey VARCHAR(225) NOT NULL, FOREIGN KEY (user) REFERENCES userlist(user))" 
               ]
    for query in comList:
        try:
            mycursor.execute(query)
            status = True
        except errors.DatabaseError as e:
            if e.errno == 1007:
                printc("[yellow][!] Database already exits.[/yellow]")
            status = False
    if status:
        printc("[gree][+] Installation completed. You're ready to use APM![/green]")
    else:
        printc("[red] [x]Installation failed.[/red]")
    mydb.close()
    
def dropDB():
    mydb = connectDB()
    mycursor = mydb.cursor()
    comList = ["DROP DATABASE userpass"]
    for query in comList:
        try:
            mycursor.execute(query)
            printc("[green][ 🗸] Database deleted successfully.[/green]")
        except Exception as e:
            printc(f"[red]{e}[/red]")
    mydb.close()
class updateDB:
    def update(self, user, password):
        mydb = connectDB()
        mycursor = mydb.cursor()
        sql = "INSERT INTO userlist (user, password) VALUES (%s, %s)"
        val = (user, password)
        try:
            mycursor.execute("USE userpass")
            mycursor.execute(sql, val)
        except Exception as e:
            printc(f"[red]{e}[/red]")
        mydb.commit()
        mydb.close()
    
    def checkUser(self, user):
        mydb = connectDB()
        mycursor = mydb.cursor()
        try:
            mycursor.execute("USE userpass")
            query = "SELECT * FROM userlist WHERE user = %s"
            mycursor.execute(query,(user,))
            result = mycursor.fetchone()
            if result:
                printc("[red][x] Username already exits. Try again...[/red]")
            else:
                return True
        except Exception as e:
            printc(f"[red]{e}[/red]")
        mydb.close()

    def userAuth(self, user, password):
        mydb = connectDB()
        mycursor = mydb.cursor()
        try:
            mycursor.execute("USE userpass")
            query = "SELECT * FROM userlist WHERE user = %s AND password = %s"
            mycursor.execute(query, (user, password))
            result = mycursor.fetchone()
            if result:
                printc(f"[green]Verified. Hello {user}.[/green]")
                return True
            else:
                printc("[red][x]Access denied.[/red]")
                return False
        except Exception as e:
            printc(f"[red]e[/red]")
        mydb.close()