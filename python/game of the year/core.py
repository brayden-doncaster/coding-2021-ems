
#import game moduals
import rps
import diceroll

print("brayden doncasters game colection")
print()
print()
print()
print()
print()
print()
print()

def menu():
    print("please select a game from below")
    print()
    print("1 - rock paper scissors")
    print("2 - dice roller")
    print("0 - exit")
    print()
    menusel = input("enter a number: ")
 

    if menusel == "0":
        exit()
    elif menusel == "1":
        rps()
    elif menusel == "2":
        diceroll()
    else:
        print("enter a valid number")
        menu()


menu()
