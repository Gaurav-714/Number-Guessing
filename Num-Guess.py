import random
import Logo_Art

EASY_LEVEL_ATTEMPS = 10
HARD_LEVEL_ATTEMPS = 5

def set_difficulty(level):

    if level == 'EASY' or level == 'Easy' or level == 'easy':
        return EASY_LEVEL_ATTEMPS
    elif level == 'HARD' or level == 'Hard' or level == 'hard':
        return HARD_LEVEL_ATTEMPS
    else:
         return  
    
def check_answer(guessed_number, answer, attempts):
    while attempts > 1:
        if guessed_number < answer:
            print("\n ' Your Guess Is Low... ' ")
            if answer - guessed_number <= 5:
                print(" > But You Are Close < ")
                if answer - guessed_number <= 3:
                    print(">> You Are Almost There <<")
            elif answer - guessed_number >= 10:
                print(">> And You Are Too Far <<")
            return attempts-1

        elif guessed_number > answer:
            print("\n ' Your Guess Is High... ' ")
            if guessed_number - answer <= 5:
                print(" > But You Are Close < ")
                if guessed_number - answer <= 3:
                    print(">> You Are Almost There <<")
            elif guessed_number - answer >= 10:
                print(">> And You Are Too Far <<")
            return attempts-1

        else:
            print(f"\n *** Hey,Congrats..You Won ***\n \
    *** Your Guess Is Right ***\n *** The Number Was < {answer} > ***\n")
    return 0

def play():

    print(Logo_Art.logo)

    print("\nLet me think of a Number between '0' to '50'\n")
    answer = random.randint(0,50)

    level = input("Choose the level of difficulty.. Input 'EASY' or 'HARD': ")
    attempts = set_difficulty(level)

    if attempts != EASY_LEVEL_ATTEMPS and attempts != HARD_LEVEL_ATTEMPS:
        print("\nYou have entered Invalid Level.. Enter Again.!!\n")
        play()
    
    guessed_number = 0    
    while guessed_number != answer:

        if attempts > 1:
            print(f"\nYou have {attempts} Attempts Left to Guess the Number..")
        else:
            print(f"\nYou have {attempts} Attempt Left to Guess the Number..")

        guessed_number = int(input("Guess a Number : "))

        attempts = check_answer(guessed_number, answer, attempts)

        if attempts == 0:
            print("\nYou are out of Attempts.. You Lose.!!")
            print(f"*** The Number Was < {answer} > ***\n")
            return
        elif guessed_number != answer:
            print(" Guess Again.. ")
        
    response = input("Do you want to Play Again.. Enter 'Yes' or 'No' : ")

    if response == 'Yes' or response == 'yes':
        play()
    elif response == 'No' or response == 'no':
        exit()
    else:
        print("Invalid Response.!!")
    
play()