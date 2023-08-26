import random
from game_logo import logo,vs
from game_data import data
import os

score = 0
# Display Higher Lower art
print(logo)
chosen_second_data = random.choice(data)
def formatData(account):
    """Format the data"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}."

# Generate a random data from data list
# Make Game Repeatable
is_game_over = True

while is_game_over:
    chosen_first_data = chosen_second_data
    chosen_second_data = random.choice(data)
    if chosen_first_data == chosen_second_data:
        chosen_second_data = random.choice(data)

    print(f"Compare A: {formatData(chosen_first_data)}")
    # Display second logo
    print(vs)
    print(f"Against B: {formatData(chosen_second_data)}")

    # Ask user to guess whose followers are more and use if statement to check correct
    guess = input("Who has more followers: Type 'A' or 'B': ").lower()
    first_follower_count = chosen_first_data["follower_count"]
    second_follower_count = chosen_second_data["follower_count"]
    # if user guess correct then clear screen and print You give correct answer
    # Keep score tracking
    if first_follower_count > second_follower_count and guess == "a":
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score: {score}.")
    # if user guess wrong then clear screen print you give wrong answer
    elif first_follower_count < second_follower_count and guess == "b":
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        is_game_over = False