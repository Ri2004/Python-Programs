import random
from art import logo,vs
from game_data import data

print(logo)

score = 0
chosen_first_data = random.choice(data)

print("Compare A:",end=" ")
for key1 in chosen_first_data:
  if key1 != "follower_count":
    print(f"{chosen_first_data[key1]},",end=" ")

print()

print(vs)

print("Against B: ",end=" ")
chosen_second_data = random.choice(data)

for key2 in chosen_second_data:
  if key2 != "follower_count":
    print(f"{chosen_second_data[key2]},",end=" ")

print()

A = chosen_first_data["follower_count"]
B = chosen_second_data["follower_count"]

answer = input("Who has more followers? Type 'A' or 'B': ")
if answer == "A" and A>B:
  score += 1
  print(f"You're right! Current score: {score}.")
else:
  print(f"Sorry, that's wrong. Final score: {score}")