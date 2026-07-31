print("****************************NUMBER GUESSING GAME***********************")
import random
number=random.randint(1,51)

print("Welcome to the Number Guessing Game!")
print("GUESS THE NUMBER BETWEEN 1 TO 50")
print("YOU HAVE 3 CHANCE")

for i in range(3):
    guess=int(input("enter your guess number="))
    
    if guess==number:
        print("You Win!🎉🎉")
        break
    elif guess>number:
        print("Too High Number")
    elif guess<number:
        print("Too Low Number")
else:
    print("You Lost The Game")
    print("Number was:",number)
