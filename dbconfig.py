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

    query = ""
    mycursor.execute(query)

except Exception as e:
    printc(f"[red]{e}[/red]")