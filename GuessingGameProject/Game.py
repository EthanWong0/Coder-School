import random

def guessingGame():
    randomNumber = random.randint(1, 3)
    guessedNumber = int(input("Guess a number from 1 to 3: ")) #Casted as an interger with int(), input() returns String datatype normally.
    tries = 1
    while tries != 3: #Condition for loop to end
        print("Tries used: ", tries)
        if randomNumber == guessedNumber: #guessedNumber cast as an interger in order to run if statement. Cannot compare an interger and a String.
            print("Correct!")
            break #Ends loop prematurely 
        else:
            tries += 1
            guessedNumber = input("Try again! ")
    if tries == 3: 
        print("Out of tries.")
        print("Correct number was",randomNumber)

guessingGame()
   
