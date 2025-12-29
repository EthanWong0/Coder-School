import random

def diceRoll():
    diceResult1 = random.randint(1, 6)
    diceResult2 = random.randint(1,6)
    diceTotal = diceResult1 + diceResult2

    print("Dice 1:", diceResult1)
    print("Dice 2:", diceResult2)
    if(diceTotal >= 6):
        print("Total number is:", diceTotal, "||", "You Won!") #Win condition is a total roll greater or equal to 6.
    else:
        print("Total number is:", diceTotal, "||", "Try again!")

diceRoll()