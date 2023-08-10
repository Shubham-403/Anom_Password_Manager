from dbconfig import createDB, dropDB
from passGen import passGen, passLen
from cryptoGraphy import encryption, decryption
from rich import print as printc
from login import login, createAccount

def logged_in(userID):
    print(userID)
    userInput= input("""
    Hello, how may I help you today?
    1. Delete all passwords.
    2. Quit.

    Enter your choice (1/2): """)
    
    if userInput == "1":
        dropDB()
    elif userInput == "2":
        printc("[green][ 🗸] Logged out.[/green]")
        printc("[green]Thankyou, have a nice day.[/green]")

        
userInput= input("""
Hello, how may I help you today?
1. Install.
2. Login.
3. Creating Account.
4. Quit.

Enter your choice (1/2/3/4): """)

if userInput == "1":
    createDB()
elif userInput == "2":
    loginStatus, userID = login()
    if loginStatus:
        logged_in(userID)
elif userInput == "3":
    createAccount()
elif userInput == "4":
    printc("[green]Thankyou, have a nice day.[/green]")


    



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
