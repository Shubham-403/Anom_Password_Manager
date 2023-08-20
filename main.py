from dbconfig import createDB, dropDB
from passGen import passGen, passLen
from cryptoGraphy import encryption, decryption
from rich import print as printc
from login import login
import os
class main:

    def clearTerminal(self):
        try:
            os.system("clear")
            os.system("cls")
        except Exception:
            pass
    
    def logged_in_pg(self,userID):
        print("[1] Delete all passwords.")
        print("[2] Sign out.")
        print("[3] Quit.")
        userInput = input("Please select an option (1/2/3): ")
        self.clearTerminal()
        
        if userInput == "1":
            dropDB()
            return True
        elif userInput == "2":
            printc("[green][ 🗸] Logged out.[/green]")
            return True
        elif userInput == "3":
            printc("[green][ 🗸] Logged out.[/green]")
            return False
        else:
            printc("[yellow] [x]Invalid input.[/yellow]")


    def loginPg(self):
        printc("-----[bold cyan]Welcome to the Anom Password Manager(APM)![/bold cyan]-----")
        print("Hello, how may I assist you today?")
        print("[1] Install Password Manager.")
        print("[2] Login.")
        print("[3] Create an Account.")
        print("[4] Quit.")
        userInput = input("Please select an option (1/2/3/4): ")
        self.clearTerminal()
        return userInput
    
    def run(self):
        self.clearTerminal()
        runningStatus = True
        while runningStatus is True:
            userInput = self.loginPg()
            if userInput == "1":
                createDB()
            elif userInput == "2":
                obj = login()
                loginStatus, userID = obj.loginAuth()
                if userID is "None":
                    self.clearTerminal()
                    printc("[yellow][!] No user account found. Please create an account.[/yellow]")
                elif loginStatus:
                    self.clearTerminal()
                    printc(f"[green][+] Login successful.[/green]")
                    printc(f"[green]Welcome back, {userID}![/green]")
                    runningStatus = self.logged_in_pg(userID)
                elif loginStatus is False:
                    printc("[red][x]Access denied.[/red]")
                
            elif userInput == "3":
                obj = login()
                status = obj.createAccount()
                if status:
                    self.clearTerminal()
            elif userInput == "4":
                runningStatus = False
                printc("[bold green]Thank you for using Anom Password Manager. Goodbye![/bold green]")
            else:
                printc("[red][x] Invalid option. Please choose a valid option.[/red]")

if __name__ == "__main__":
    app = main()
    app.run()


    



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
