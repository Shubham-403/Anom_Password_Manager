import random 
from rich import print as printc
import string

l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)


def passLen():
    printc("[green]Character length: [/green]", end="")
    length = int(input())
    # if 4 > length < 16 and (length%2)!= 0 :
    #     while (length%2) != 0 or 4 > length < 16 :
    #         printc("[red] [x] Invalid input. Please try again...[/red] ")
    #         printc("[green]Character length (even, >4 and <16 ): [/green]", end="")
    #         length = int(input())
    return length

def passGen(passLen):
    password = ""
    l = random.randrange(1, 5)
    for i in range(passLen):
        if l == 1:
            lst = l1
        elif l == 2:
            lst = l2
        elif l == 3:
            lst = l3
        elif l == 4:
            lst = l4
            l = 0
        
        password = password + random.choice(lst)
        l+=1
        
    return password

