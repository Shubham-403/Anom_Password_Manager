import mysql.connector
from rich import print as printc
def connectDB():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "password_manager"
        ) 
        printc("[green][ 🗸] Database connected.[/green]")
    except Exception as e:
        printc(f"[red]{e}[/red]")
    return mydb

def createDB():
    mydb = connectDB()
    mycursor = mydb.cursor()
    comList = ["CREATE DATABASE passuser", 
               "USE passuser","CREATE TABLE passlist(user VARCHAR(225),webName VARCHAR(225) NOT NULL, url VARCHAR(225) NOT NULL, mail VARCHAR(225) NOT NULL, id VARCHAR(225) NOT NULL, password VARCHAR(225) NOT NULL, note VARCHAR(225), encryptionKey VARCHAR(225) NOT NULL, PRIMARY KEY(user))", 
               "CREATE TABLE userlist(user VARCHAR(225), password VARCHAR(225), FOREIGN KEY (user) REFERENCES passlist(user))"]
    for query in comList:
        try:
            mycursor.execute(query)
        except Exception as e:
            printc(f"[red]{e}[/red]")
    
def dropDB():
    mydb = connectDB()
    mycursor = mydb.cursor()
    comList = ["DROP DATABASE passuser"]
    for query in comList:
        try:
            mycursor.execute(query)
            printc("[green][ 🗸] Database deleted successfully.[/green]")
        except Exception as e:
            printc(f"[red]{e}[/red]")