from rich import print as printc
import maskpass

def login():
    maxAttempts = 3
    attempt = 0
    logged_in = False
    userID = None
    while attempt<maxAttempts and not logged_in:
        if attempt==1:
            printc("[red][x]Login failed. Invalid User_ID or Master_Password.[/red] (2 attempts remaining)")
        elif attempt == 2:
            printc("[red][x]Login failed. Invalid User_ID or Master_Password.[/red] (1 attempts remaining)")

        userID = input("User_ID: ")
        masterPassword = maskpass.askpass(prompt="Master_Password: ", mask='*')
        if userID == "shubham" and masterPassword == "root":
            logged_in = True
        else:
            logged_in = False
        attempt +=1
    if logged_in:
        printc("[green]Login successful![/green]")
    else:
        printc("[red][x]Access denied.[/red]")
    return logged_in, userID

def createAccount():
    status = False
    while status is False:
        userID = input("User_ID: ")
        if not userID:
            printc("[red][x] User_ID cannot be empty![/red]")
        elif userID:
            masterPassword = maskpass.askpass(prompt="Master_Password: ", mask='*')
            if not masterPassword:
                printc("[red][x] Master_Password cannot be empty![/red]")
            elif masterPassword:
                masterPassword1 = maskpass.askpass(prompt="Re-enter Master_Password: ", mask='*')
                if masterPassword == masterPassword1:
                    status = True
                    printc(f"[green][+] Account created. Your User_ID is {userID}[/green]")
                elif masterPassword != masterPassword1:
                    printc("[red][x] The re-entered Master_Password does not match. Please try again... [/red]")
        

