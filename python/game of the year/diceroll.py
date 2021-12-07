#import packages
import random

#import menu funcion
import core

def diceroll():
    numb = random.randint(1,6)

    print(f"your number is {numb}")


    print("please select what to do next")
    print()
    print("1 - play again")
    print("2 - menu")
    print("3 - exit")
    print()       
    wdn = input("enter a number: ")

    if wdn == "1":
        diceroll()
    elif wdn == "2":
        core.menu()
    elif wdn == "3":
        exit()
    else:
        print("enter a valid number")

