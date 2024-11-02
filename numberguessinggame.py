from random import randint

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

#function to check user guess against actual answer
def check_number(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too High")
        return turns-1
    elif user_guess < actual_answer:
        print("Too low")
        return turns-1
    else:
        print(f"You Got it! The answer was {actual_answer}")
    
#Function to set difficulty
def set_difficulty():
    level=input("Choose difficulty.Type 'easy' or 'hard': ")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
#choosing a number between 1 to 100
def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100")
    answer=randint (1,100)

    turns=set_difficulty()
     

    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess a number.")
        #Let the user guess the number
        guess=int(input("Make a guess: "))
        turns=check_number(guess,answer,turns)
        if turns==0:
            print("You've ran out of guesses,you lose.")
            print(f"PSsst, the correct answer is {answer}")
            return
        elif guess!=answer:
            print("Guess again!")
game()

