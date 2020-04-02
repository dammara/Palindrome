# Markhus Dammar
# 30 March 2020
# This program will use a recursive formula to check if a string is a Palindrome or not.

import time


def true():
    print("This string is a Palindrome.")


def false():
    print("This string is not a Palindrome.")


def p_check(string):
    string.strip()
    string = string.lower().replace(" ", "")
    print(string)
    if len(string) < 1:      # BASE CASE
        true()
    elif string[0] == string[-1]:
            return p_check(string[1:-1])    # Will check each letter until base case is reached
    else:
        false()


def welcome():
    print("""
    Welcome. Please enter a word or sentence and 
    we'll check if it is a Palindrome or not.""")
    usrstring = str(input(">>>"))
    p_check(usrstring)
    time.sleep(2)


def next():
    print("Now what?")
    choice = int(input("""
    TYPE 1 or 2
        1. Restart
        2. Exit
        >>>"""))
    if choice == 1:
        welcome()
    elif choice == 2:
        exit()
    else:
        print("INVALID")
        time.sleep(1)
        next()

# Program starts here
welcome()
next()
