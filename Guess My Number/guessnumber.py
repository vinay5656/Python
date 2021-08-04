from art1 import logo1
from art2 import logo2
import random

print("Welcome to the Number Guess Game !")
# myNumber = random.randrange(1,101)
# print(myNumber)
again = True
areYouSuccesssed = False
def campareNumber(number_1,number_2) :
    if number_1==number_2 : 
        areYouSuccesssed = True
        return "Correct Guess"
    else : 
        return "Too low" if number_1 > number_2 else "Too high"

def guessNumber(attempts) : 
    isItYourNumber = int(input("Guess a number"))
    whatsAboutNumber=campareNumber(myNumber,isItYourNumber)
    print(whatsAboutNumber)
    if whatsAboutNumber != "Correct Guess" :
        return attempts - 1
    return 0
while again == True :
    myNumber = random.randrange(1,101)
    print(myNumber)
    difficultyLevel = input("chosse a difficulty level : Hard or Easy : ")
    if difficultyLevel == "Hard" :
        print(logo2)
        attempts = 5
        remainingAttempts = guessNumber(attempts)
        while not areYouSuccesssed and remainingAttempts>0 :
            print(f"You have {remainingAttempts} attempts remaining to guess the number")
            remainingAttempts=guessNumber(remainingAttempts)
            
    elif difficultyLevel == "Easy" :
        print(logo1)
        attempts = 10
        remainingAttempts = guessNumber(attempts)
        while not areYouSuccesssed and remainingAttempts>0 :
            print(f"You have {remainingAttempts} attempts remaining to guess the number")
            remainingAttempts=guessNumber(remainingAttempts)
    
    else :
        print("Please choose a difficulty level")
    
    if input("Do you want to play Again y/n") == "n":
        again=False
