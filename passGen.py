import random
import string
from rich import print as printc

class generator():
    l1 = list(string.ascii_lowercase)
    l2 = list(string.ascii_uppercase)
    l3 = list(string.digits)
    l4 = list(string.punctuation)


    def passLen():
        printc("[green]Character length: [/green]", end="")
        length = int(input())
        return length

    def passGen(passLen):
        password = ""
        l = random.randrange(1, 5)
        for i in range(int(passLen)):
            if l == 1:
                lst = generator.l1
            elif l == 2:
                lst = generator.l2
            elif l == 3:
                lst = generator.l3
            elif l == 4:
                lst = generator.l4
                l = 0
            
            password = password + random.choice(lst)
            l+=1
            
        return password
