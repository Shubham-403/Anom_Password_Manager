import random 
from rich import print as printc
import string

l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

condition = False
def passLen():
    length = int(input("Character length (even): "))
    while (length%2) != 0:
        printc("[red][x] Invalid input.[/red] ")
    

print(passLen())
    
