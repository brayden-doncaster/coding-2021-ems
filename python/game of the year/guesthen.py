#import packages
import random

#import game files
import core

def gtn():
    print("what range do you want")
    print()
    print("1 - 1 to 5")
    print("2 - 1 to 10")
    print("3 - 1 to 100")
    print("4 - 1 to 1000")
    print()
    selgtn = input("please select from above: ")

    low = 1
    high = 5

    if selgtn == "1":
        high = 5
    elif selgtn == "2":
        high = 10
    elif selgtn == "3":
        high = 100
    elif selgtn == "4":
        high = 1000
    else:
        print("enter a valid number")
        gtn()

    computer = random.randint(low,high)

    player = input(f"what is your guess. ({low} to {high}) ")

    try:
        computer = int(computer)
        player = int(player)
    except:
        print("something went wrong")

    if player > computer:
        print(f"you were to high. the number was {computer}. you guessed {player}.")
    elif player < computer:
        print(f"you were to low. the number was {computer}. you guessed {player}.")
    elif player == computer:
        print(f"you were corect it was {computer} and you guessed {player}")
    else:
        print("something when wrong.")

    print()
    print()

    print("please select what to do next")
    print()
    print("1 - play again")
    print("2 - menu")
    print("3 - exit")
    print()       
    wdn = input("enter a number: ")

    if wdn == "1":
        gtn()
    elif wdn == "2":
        core.menu()
    elif wdn == "3":
        exit()
    else:
        print("enter a valid number")