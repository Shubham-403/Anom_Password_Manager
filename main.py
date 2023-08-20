from dbconfig import createDB, dropDB
from passGen import passGen, passLen
from cryptoGraphy import encryption, decryption
from rich import print as printc
from login import login, createAccount

def loginPg():
    printc("-----[bold cyan]Welcome to the Anom Password Manager(APM)![/bold cyan]-----")
    print("Hello, how may I assist you today?")
    print("[1] Install Password Manager.")
    print("[2] Login.")
    print("[3] Create an Account.")
    print("[4] Quit.")
    userInput = input("Please select an option (1/2/3/4): ")
    return userInput

def logged_in_pg(userID):
    printc(f"Welcome, {userID}")
    print("[1] Delete all passwords.")
    print("[2] Sign out.")
    print("[3] Quit.")
    userInput = input("Please select an option (1/2/3): ")
    
    if userInput == "1":
        dropDB()
    elif userInput == "3":
        printc("[green][ 🗸] Logged out.[/green]")
        printc("[bold]Thank you for using Anom Password Manager. Goodbye![/bold]")
    else:
        printc("[yellow] [x]Invalid input.[/yellow]")



runningStatus = True
while runningStatus is True:
    userInput = loginPg()
    if userInput == "1":
        createDB()
    elif userInput == "2":
        loginStatus, userID = login()
        if loginStatus:
            logged_in_pg(userID)
    elif userInput == "3":
        createAccount()
    elif userInput == "4":
        runningStatus = False
        printc("[bold]Thank you for using Anom Password Manager. Goodbye![/bold]")
    else:
        printc("[red][x] Invalid option. Please choose a valid option (1/2/3/4).[/red]")


    



# password = passGen(passLen())
# print(password)

# hash, key = encryption(password)
# print(hash)
# print(key)

# decript = decryption(key, hash)
# print(decript)


# userInput = loginPg()
# if userInput == 1:
#     print("1")
# elif userInput ==2:
#     print("2")
# else:
#     printc("[red][x] Invalid input. Please try asgain.[/red]")


# createDB()
# dropDB()
