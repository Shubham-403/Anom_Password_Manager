import os
from rich import print as printc

from login import login
from pipconfig import installReq
from passgen import generator
from dbconfig import updatePassDB, createDB, dropDB


class main:    
    def clearTerminal(self):
        try:
            os.system("clear")
            os.system("cls")
        except Exception:
            pass
    
    def logged_in_pg(self,userID):
        runningStatus = True
        while runningStatus:
            print("[1] Retrieve a password.")
            print("[2] Add a new password.")
            print("[3] Delete all passwords.")
            print("[4] Sign out.")
            print("[5] Quit.")
            userInput = input("Please select an option (1/2/3/4/5): ")
            self.clearTerminal()
            
            if userInput == "1":
                pass
            elif userInput == "2":
                website = input("Website name: ")
                url = input("Website URL: ")
                mail = input("Mail: ")
                id = input("Website User ID: ")
                password = input("Password: ")
                note = input("Note(Write 'null' if no note): ")
                status = updatePassDB.update(userID, website, url, mail, id, password, note)
                self.clearTerminal()
                if status:
                    printc("[green][+] New Password added.[/green]")
                else:
                    printc("[yellow][x] Failed.[/yellow]")
            elif userInput == "3":
                dropDB()
                return True
            elif userInput == "4":
                printc("[green][ 🗸] Logged out.[/green]")
                return True
            elif userInput == "5":
                printc("[green][ 🗸] Logged out.[/green]")
                printc("[bold green]Thank you for using Anom Password Manager. Goodbye![/bold green]")
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
                obj = installReq()
                #obj.installPackages()
                createDB()
            elif userInput == "2":
                obj = login()
                loginStatus, userID = obj.loginAuth()
                if userID is "None":
                    self.clearTerminal()
                    printc("[yellow][!] No user account found. Please create an account.[/yellow]")
                elif loginStatus:
                    self.clearTerminal()
                    printc("[green][+] Login successful.[/green]")
                    printc(f"[green]Welcome back, {userID}![/green]")
                    runningStatus = self.logged_in_pg(userID)
                elif loginStatus is False:
                    self.clearTerminal()
                    printc("[red][[/red][red]x[/red][red]][red] Access denied.[/red]")
                
            elif userInput == "3":
                obj = login()
                status, userID = obj.createAccount()
                if status:
                    self.clearTerminal()
                    printc(f"[green][+] Account created successfully. Welcome to Anom Password Manager, {userID}![/green]")
            elif userInput == "4":
                runningStatus = False
                printc("[bold green]Thank you for using Anom Password Manager. Goodbye![/bold green]")
            else:
                printc("[red][x] Invalid option. Please choose a valid option.[/red]")

if __name__ == "__main__":
    app = main()
    app.run()
