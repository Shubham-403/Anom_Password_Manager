from rich import print as printc
import maskpass
from dbconfig import updateDB

def login():
    maxAttempts = 3
    attempt = 0
    logged_in = False
    userID = None
    updater = updateDB()
    while attempt<maxAttempts and not logged_in:
        if attempt==1:
            printc("[red][x]Login failed. Invalid User_ID or Master_Password.[/red] (2 attempts remaining)")
        elif attempt == 2:
            printc("[red][x]Login failed. Invalid User_ID or Master_Password.[/red] (1 attempts remaining)")

        userID = input("User_ID: ")
        masterPassword = maskpass.askpass(prompt="Master_Password: ", mask='*')
        if updater.userAuth(userID, masterPassword) == True:
            logged_in = True
        else:
            logged_in = False
        attempt +=1
    if logged_in:
        printc(f"[green][+] Login successful. Welcome back, {userID}![/green]")
    else:
        printc("[red][x]Access denied.[/red]")
    return logged_in, userID

def createAccount():
    status = False
    updater = updateDB()
    while status is False:
        userID = input("Choose a username: ")
        if not userID:
            printc("[red][x] User_ID cannot be empty![/red]")
        elif " " in userID:
            printc("[yellow][!] Warning: User_ID cannot contain spaces. Please remove spaces and try again.[/yellow]")
        elif userID and updater.checkUser(userID):
            masterPassword = maskpass.askpass(prompt="Create a Master_Password: ", mask='*')
            if not masterPassword:
                printc("[red][x] Master_Password cannot be empty![/red]")
            elif masterPassword:
                masterPassword1 = maskpass.askpass(prompt="Re-enter your Master_Password: ", mask='*')
                if masterPassword == masterPassword1:
                    status = True
                    printc(f"[green][+] Account created successfully. Welcome to Anom Password Manager, {userID}![/green]")
                elif masterPassword != masterPassword1:
                    printc("[red][x] The re-entered Master_Password does not match. Please try again... [/red]")

    if status == True:
        updater.update(userID, masterPassword)
        

