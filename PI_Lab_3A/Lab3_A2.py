import string
from symtable import Symbol

password = input("Enter password: ")
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
isReliable = True

if(len(password) != 8):
    print("The password length is not equal to 8")
    isReliable = False
if(password.lower() == password):
    print("The password does not contain uppercase letters")
    isReliable = False
if(password.upper == password):
    print("The password does not contain lowercase letters")
    isReliable = False
if(any(symbol.isdigit() for symbol in password) == False):
    print("The password does not contain any digits")
    isReliable = False
if(any(symbol == '*' or symbol == '_' or symbol == '*' for symbol in password)):
    print("The password does not contain special characters")
    isReliable = False
if(all(symbol in allowed for symbol in password) == False):
    print("The password contains unsupported characters")
    isReliable = False

if (isReliable):
    print("Strong password")