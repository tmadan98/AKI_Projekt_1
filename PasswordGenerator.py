import random
from wypp import *
import string

def generatePassword(length: int):

    pwsd = ""

    lowercase = list(string.ascii_lowercase)   
    uppercase = list(string.ascii_uppercase)  
    digits    = list(string.digits)
    symbols   = list(string.punctuation)

    all = lowercase + uppercase + digits + symbols
    for x in range(length):
        index = random.randint(0, len(all)-1)
        pwsd += all[index]
    
    print(f"Heres your new password: {pwsd}")


def passwordLength()-> int:
    
    try: 
        length = int(input("Enter length of password:"))
    except:
        print("You need to enter a value of type 'int'!")
        passwordLength()
    else:
        generatePassword(length)


passwordLength()