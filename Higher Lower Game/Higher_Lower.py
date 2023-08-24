import random
from game_logo import logo,vs
from game_data import data
import os

def formatName(account_data):
  account_name = account_data["name"]
  account_description = account_data["description"]
  account_country = account_data["country"]
  
  return f"{account_name}, a {account_description}, from {account_country}."

print(logo)

def printLogo():
  print(logo)

score = 0
chosen_first_data = random.choice(data)

print(f"Compare A: {formatName(chosen_first_data)}")

print(vs)

chosen_second_data = random.choice(data)
print(f"Against B: {formatName(chosen_second_data)}")

if chosen_first_data == chosen_second_data:
  chosen_second_data = random.choice(data)
  
A = chosen_first_data["follower_count"]
B = chosen_second_data["follower_count"]

is_game_over = False
while not is_game_over:
  answer = input("Who has more followers? Type 'A' or 'B': ")
  if answer == "A" and A>B:
    score += 1
    os.system('clear')
    printLogo()
    print(f"You're right! Current score: {score}.")
  
    chosen_first_data = chosen_second_data.copy()
    print(f"Compare A: {formatName(chosen_first_data)}")
  
    print(vs)
    chosen_second_data = random.choice(data)

    if chosen_first_data == chosen_second_data:
      chosen_second_data = random.choice(data)
      
    print(f"Against B: {formatName(chosen_second_data)}")
  else:
    os.system('clear')
    printLogo()
    print(f"Sorry, that's wrong. Final score: {score}")
    is_game_over = True