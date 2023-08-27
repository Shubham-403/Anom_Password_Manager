import maskpass
from rich import print as printc

from dbconfig import updateDB
from cryptoGraphy import cryptoGraphy

class login:
    def loginAuth(self):
        updater = updateDB()
        logged_in = False
        userID = None
        result = updater.userDataCheck() 
        if result == "NoDB":
            userID = "None"
            printc("[red][!] Database doesn't exist. Please install the software from the homepage.[/red]")
        elif result == "None":
                userID = "None"
                printc("[yellow][!] No user account found. Please create an account.[/yellow]")
        elif result:
            maxAttempts = 3
            attempt = 0
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
        return logged_in, userID

    def createAccount(self):
        status = False
        updater = updateDB()
        results = updater.DBCheck()
        if results:
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
                        elif masterPassword != masterPassword1:
                            printc("[red][x] The re-entered Master_Password does not match. Please try again... [/red]")
        elif results is False:
            printc("[yellow][!] Database doesn't exist. Please install the software from the homepage.[/yellow]")
        if status == True:
            key = cryptoGraphy.genKey()
            encrypted_masterPassword = cryptoGraphy.encrypt(key, masterPassword)
            updater.update(userID, encrypted_masterPassword, key)
        return status, userID
            

