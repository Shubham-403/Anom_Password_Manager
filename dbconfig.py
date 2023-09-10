import mysql.connector
from rich import print as printc
from mysql.connector import errors
from cryptoGraphy import cryptoGraphy


class connectionDB:
    def connectDB(self):
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "root"
            ) 
        except Exception as e:
            printc(f"[red]{e}[/red]")
        return mydb

    def createDB(self):
        mydb = self.connectDB()
        mycursor = mydb.cursor()
        comList = ["CREATE DATABASE userpass",
                "USE userpass",
                "CREATE TABLE userlist(user VARCHAR(225), password VARCHAR(225), cryptographyKey VARCHAR(225), PRIMARY KEY (user))",
                "CREATE TABLE passlist(user VARCHAR(225),webName VARCHAR(225) NOT NULL, url VARCHAR(225) NOT NULL, mail VARCHAR(225) NOT NULL, id VARCHAR(225) NOT NULL, password VARCHAR(225) NOT NULL, note VARCHAR(225), FOREIGN KEY (user) REFERENCES userlist(user))" 
                ]
        for query in comList:
            try:
                mycursor.execute(query)
                status = True
            except errors.DatabaseError as e:
                if e.errno == 1007:
                    printc("[yellow][!] Database already exits.[/yellow]")
                status = "None"
        if status is True:
            printc("[green][+] Installation completed. You're ready to use APM![/green]")
        elif status == "None":
            pass
        else:
            printc("[red] [x]Installation failed.[/red]")
        mydb.close()

    def dropDB(self):
        mydb = self.connectDB()
        mycursor = mydb.cursor()
        comList = ["DROP DATABASE userpass"]
        for query in comList:
            try:
                mycursor.execute(query)
                printc("[green][ 🗸] Database deleted successfully.[/green]")
            except Exception as e:
                printc(f"[red]{e}[/red]")
        mydb.close()

    def DBCheck(self):
        mydb = self.connectDB()
        mycursor = mydb.cursor()
        status = None
        try:
            mycursor.execute("USE userpass")
            status = True
        except errors.DatabaseError as e:
            if e.errno == 1049 :
                status = False
        mydb.close()
        return status

class userList:
    db_connection = connectionDB()
    def addUser(self, user, password, key):
        mydb = self.db_connection.connectDB()
        mycursor = mydb.cursor()
        sql = "INSERT INTO userlist (user, password, cryptographyKey) VALUES (%s, %s, %s)"
        val = (user, password, key)
        try:
            mycursor.execute("USE userpass")
            mycursor.execute(sql, val)
        except Exception as e:
            printc(f"[red]{e}[/red]")
        mydb.commit()
        mydb.close()

    def removeUser(self, user):
        pass

    def authUser(self, user, password):
        mydb = self.db_connection.connectDB()
        mycursor = mydb.cursor()
        try:
            mycursor.execute("USE userpass")
            query = "SELECT * FROM userlist WHERE user = %s"
            mycursor.execute(query, (user,))
            userDB, passwordDB, cryptograhyKeyDB = mycursor.fetchone()
            decryptedPass = cryptoGraphy.decrypt(cryptograhyKeyDB, passwordDB)
            if password == decryptedPass:
                return True
            else:
                printc("[red][x]Access denied.[/red]")
                return False
        except Exception as e:
            printc(f"[red]{e}[/red]")
        mydb.close()

    def is_username_available(self, user):
        mydb = self.db_connection.connectDB()
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

    def does_user_exist(self):
        mydb = self.db_connection.connectDB()
        mycursor = mydb.cursor()
        try:
            mycursor.execute("USE userpass")
            mycursor.execute("SELECT * FROM userlist")
            result = mycursor.fetchone()
            if result:
                return True
            else:
                return "None"
        except errors.DatabaseError as e:
            if e.errno == 1049:
                return "NoDB"
        mydb.close()

class passList:
    db_connection = connectionDB()
    def addPass(self,user, webName, url, mail, id, password, note):
        mydb = self.db_connection.connectDB()
        mycursor = mydb.cursor()
        
        try:
            sql = ("SELECT cryptographyKey FROM userlist WHERE user=%s")
            mycursor.execute("USE userpass")
            mycursor.execute(sql, (user,))
            cryptoGraphyKeys = mycursor.fetchone()
            cryptoGraphyKey = cryptoGraphyKeys[0]

            encrypted_webName = cryptoGraphy.encrypt(cryptoGraphyKey, webName)
            encrypted_url = cryptoGraphy.encrypt(cryptoGraphyKey, url)
            encrypted_mail = cryptoGraphy.encrypt(cryptoGraphyKey, mail)
            encrypted_id = cryptoGraphy.encrypt(cryptoGraphyKey, id)
            encrypted_password = cryptoGraphy.encrypt(cryptoGraphyKey, password)
            dencrypted_note = cryptoGraphy.encrypt(cryptoGraphyKey, note)

            sql = "INSERT INTO passlist(user, webName, url, mail, id, password, note) VALUES(%s,%s, %s, %s, %s, %s, %s)"
            val = (user, encrypted_webName, encrypted_url, encrypted_mail, encrypted_id, encrypted_password, dencrypted_note)
            mycursor.execute("USE userpass")
            mycursor.execute(sql, val)
            status = True
        except Exception as e:
            printc(f"[red]{e}[/red]")

        mydb.commit()
        mydb.close()

        if status:
            return True
        else:
            return False
        
    def removePass():
        pass

    def retrievePass(self):
        mydb = self.db_connection.connectDB()
        mycursor = mydb.cursor()

        try:
            sql = "SELECT webName FROM passlist;"
            mycursor.execute("USE userpass")
            mycursor.execute(sql)
            result = mycursor.fe
            for webNames in result:
                print(webNames[0])

        except Exception as e:
            print(e)

myObj = passList()
myObj.retrievePass()