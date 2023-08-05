import mysql.connector
from rich import print as printc

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "password_manager"
    ) 
    printc("[green][ 🗸] Database connected.[/green]")
    mycursor = mydb.cursor()

    query = "CREATE TABLE pm ( site_name VARCHAR(225) NOT NULL, user_id VARCHAR(225), mail_id VARCHAR(225), password VARCHAR(225) NOT NULL, hashkey VARCHAR(225) NOT NULL, note VARCHAR(225))"
    mycursor.execute(query)

except Exception as e:
    printc(f"[red]{e}[/red]")

