from rich import print as printc
from pipconfig import installReq
try:
    import os
    import pyperclip

    from login import login
    from passGen import generator
    from dbconfig import connectionDB, passList
except Exception as e:
    if e:
        obj = installReq()
        obj.installPackages()

class main:    
    def clearTerminal(self):
        try:
            os.system("clear")
            os.system("cls")
        except Exception:
            pass
    def passwordGen(self):
        runningStatus = True
        while runningStatus:
            print("You can choose any one type for a password: ")
            print(" [1] Password Generator.(More Secure)")
            print(" [2] Own Password")
            choice = input("    Please select an option (1/2): ")
            if choice == "1":
                print("\n   The suggested password length is 4 to 16 characters, with longer passwords being generally more secure.")
                length = input("    Password length: ")
                password = generator.passGen(length)
                print(f"Generated secure password: {password}")
                runningStatus = False
            elif choice == "2":
                password = input("\nPassword: ")
                runningStatus = False
            else:
                printc("[yellow][!] Invalid input.[/yellow]")
                runningStatus = True
        return password
    
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
            myObj = passList()
            if userInput == "1":
                myObj.retrievePass()
            elif userInput == "2":
                website = input("Website name: ")
                url = input("Website URL: ")
                mail = input("Mail: ")
                id = input("Website User ID: ")
                password = self.passwordGen()
                note = input("Note(Write 'null' if no note): ")
                status = myObj.addPass(userID, website, url, mail, id, password, note)
                self.clearTerminal()
                if status:
                    printc("[green][+] New Password added.[/green]")
                else:
                    printc("[yellow][x] Failed.[/yellow]")
            elif userInput == "3":
                db_connection = connectionDB()
                db_connection.dropDB()
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
                obj.installPackages()
                db_connection = connectionDB()
                db_connection.createDB()
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