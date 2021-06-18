#!/usr/bin/python python3
import secrets
import sys
from pandas.io.clipboard import copy;

MIN_PASSWORD_LENGHT = 6
MIN_DIGIT_AMOUNT = 2
POSSIBLE_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
POSSIBLE_NUMBERS = "01234567890"
POSSIBLE_SPECIAL = r"!@#$%^&*()"
POSSIBLE_CHARACTERS =  POSSIBLE_LETTERS + POSSIBLE_NUMBERS + POSSIBLE_SPECIAL
NEED_LOWER = True
NEED_UPPER = True
NEED_SPECIAL = True
NEED_DIGIT = True


def GeneratePassword(_Passlength):
    while True:
        password = "".join(secrets.choice(POSSIBLE_CHARACTERS) for i in range(_Passlength))
        if ((NEED_LOWER and any(c.islower() for c in password))
            and (NEED_UPPER and any(c.isupper() for c in password)) 
            and (NEED_SPECIAL and  any(c in "!@#$%^&*()" for c in password))
            and (NEED_DIGIT and sum(c.isdigit() for c in password) >= MIN_DIGIT_AMOUNT)): 
                return password

def main(argv):
    try:
        if (len(argv) == 0):
            passlength = int(input("Enter password length: "))
        else:
            passlength = int(argv[0])
    except:
        print('GeneratePassword.py <passlength>')
        sys.exit(0)
    while True:
        passlength = max(passlength, max(MIN_PASSWORD_LENGHT, calculateMinimalPasslength()))
        print(f"Generating Password with length: {passlength}")
        password = GeneratePassword(passlength)
        print(password)
        copy(password)
        userinput = (input("Enter another password length to retry or any other input to exit: "))
        if userinput.isnumeric():
            passlength = int(userinput)
        else:
            sys.exit(0)

def calculateMinimalPasslength():
    minLength = 0
    if NEED_DIGIT:
        minLength += MIN_DIGIT_AMOUNT
    if NEED_LOWER:
        minLength += 1
    if NEED_UPPER:
        minLength += 1
    if NEED_SPECIAL:
        minLength += 1
    return minLength

if __name__ == "__main__":
    main(sys.argv[1:])


