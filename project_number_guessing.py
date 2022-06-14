import random
from art import logo
print(logo)

Number = random.randrange(1,100)
play = True  
def check(Number):
    level = input("Enter difficulty level 'easy' or 'hard': ")
    if(level=="easy"):
        attempts_left = 10 
    elif(level == "hard"):
        attempts_left = 5
    else:
        print("Invalid Input!!")
        return 

    print("Guess the Number........")
    print(f"You have {attempts_left} attempts left")

    while(attempts_left):
        attempts_left-=1
        guess = eval(input("Enter a number between 1 - 100 : "))
        if(guess == Number):
            print("\n     congratulations!!! You guessed it right🏆🏆🏆\n\n")
            return
        elif(attempts_left):
            if(guess > Number):
                print("try lower Number!!")
                print(f"you have {attempts_left} attempts left!")
            else:
                print("try higher Number!!") 
                print(f"you have {attempts_left} attempts left!")
       
    else:
        print("You lose!!😢")
        print("winning no was: ",Number," 😢")
        return 


while(play):
    check(Number)
    isplay=input("Do you want to play again ? 'y' for yes or 'n' for no ")
    if(isplay == 'n'):
        play = False
        
