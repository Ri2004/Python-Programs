#HINT: You can call clear() to clear the output in the console.
from art import logo
import os
print(logo)

auction ={}
end_bidder = False


def find_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""

  for name in bidding_record:
    amount = bidding_record[name]
    if amount > highest_bid:
      highest_bid = amount
      winner = name

  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while not end_bidder:
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What is your bid?: $"))

  auction[bidder_name] = bid_amount
  
  any_other_person = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  os.system('cls')
  if any_other_person == "no":
    os.system('cls')
    end_bidder = True

    find_highest_bid(auction)