# Guess the Number
import random
from Guess_Number_Logo import logo
print("Welcome to the Number Guessing game!")
print(logo)

print("Let me think a Number between 1 to 50")
chosen_number = random.randint(1, 50)

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_level(level):
    if level == 'easy':
        print(f"You've {EASY_LEVEL_ATTEMPTS} attempts to guess the number.")
        return EASY_LEVEL_ATTEMPTS
    
    elif level == 'hard':
        print(f"You've {HARD_LEVEL_ATTEMPTS} attempts to guess the number.")
        return HARD_LEVEL_ATTEMPTS
    
    else:
        print("You Chose wrong level")
    
level = input("Choose the difficulty level... Type easy or hard: ").lower()
attempts = check_level(level)
print(attempts)

guess = 0

while guess != chosen_number:
    guess = int(input("Guess a Number: "))
    if guess > chosen_number:
        print("Your guess is too high.")
        print("Guess again")
        attempts -= 1
        print(f"You've {attempts} attempt left to guess the number.")
        if attempts == 0:
            exit(0)
            
    elif guess < chosen_number:
        print("Your guess is too low.")
        print("Guess again")
        attempts -= 1
        print(f"You've {attempts} attempt left to guess the number.")
        if attempts == 0:
            exit(0)
            
    else:
        print(f"You got it. The answer is {guess}.")