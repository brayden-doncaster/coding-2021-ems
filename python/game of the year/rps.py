#import packages
import random

#import menu funcion
import core


def rps():
 
    set = ["rock", "paper", "scissors"]

    computer = set[random.randint(0,2)]

    print("select one from below")
    print()
    print("1 - rock")
    print("2 - paper")
    print("3 - scissors")
    print()
    player = input("enter a number: ")

    if player == "1":
        player = "rock"
    elif player == "2":
        player = "paper"
    elif player == "3":
        player = "scissors"
    else:
        print("enter a valid number")
        core.menu()
   

    if player == computer:
        print("tie to {}".format(computer))
    elif player == "rock":
        if computer == "paper":
            print("you suck and lost to paper")
        else:
            print("you win and beat scissors")
    elif player == "paper":
        if computer == "rock":
            print("you win and beat rock")
        else:
            print("you suck and lost to scissors")
    elif player == "scissors":
        if computer == "paper":
            print("you win and beat paper")
        else:
            print("you suck and lost to rock")

    print("please select what to do next")
    print()
    print("1 - play again")
    print("2 - menu")
    print("3 - exit")
    print()       
    wdn = input("enter a number: ")

    if wdn == "1":
        rps()
    elif wdn == "2":
        core.menu()
    elif wdn == "3":
        exit()
    else:
        print("enter a valid number")
