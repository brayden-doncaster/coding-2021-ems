val1 = input("enter your first number: ")
val2 = input("enter your second number: ")

try:
    val1 = float(val1)
    val2 = float(val2)
except:
    print("you must enter numbers")
    exit()

print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

print()
ans = input("select one from above: ")

if ans == "1":
    print(val1 + val2)
elif ans == "2":
    print(val1 - val2)
elif ans == "3":
    print(val1 * val2)
elif ans == "4":
    print(val1 / val2)
else:
    print("you need to input a valid input")


input("say anything to continue: ")




