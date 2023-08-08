# Guess the Number
import random
print("Let me think a Number between 1 to 50")
chosen_number = random.randint(1, 50)
print(chosen_number)

easy_level_attempts = 10
hard_level_attempts = 5
def check_level(level):
    if level == 'easy':
        print(f"You've {easy_level_attempts} attempts to guess the number.")
        return easy_level_attempts
    
    elif level == 'hard':
        print(f"You've {hard_level_attempts} attempts to guess the number.")
        return hard_level_attempts
    
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
        print("Your guess is right....")